from transformers import (
    BartTokenizer, 
    AutoTokenizer, 
    BartForConditionalGeneration, 
    PreTrainedTokenizerFast
)

import torch

MAX_LEN = 1024

class Summarizer:

    def __init__(self):
        
        # Good but slow

        # HANDLE = 'ml_kit/summary/bart-large-cnn'
        # self.tokenizer = BartTokenizer.from_pretrained(HANDLE)
        # self.model = BartForConditionalGeneration.from_pretrained(HANDLE)

        # Fast but inaccurate

        HANDLE = 'ml_kit/summary/bart-base-cnn'
        self.tokenizer = PreTrainedTokenizerFast.from_pretrained(HANDLE)
        self.model = BartForConditionalGeneration.from_pretrained(HANDLE)

        # Midway?

        # HANDLE = 'ml_kit/summary/distilbart-cnn-12-6'
        # self.tokenizer = AutoTokenizer.from_pretrained(HANDLE)
        # self.model = BartForConditionalGeneration.from_pretrained(HANDLE)

    def __call__(self, input_text:str) -> str:
                
        # tokenize without truncation
        inputs_no_trunc = self.tokenizer(input_text, max_length=None, return_tensors='pt', truncation=False)

        # get batches of tokens corresponding to the exact model_max_length
        chunk_start = 0
        chunk_end = MAX_LEN # tokenizer.model_max_length  # == 1024 for Bart
        inputs_batch_lst = []
        while chunk_start <= len(inputs_no_trunc['input_ids'][0]):
            inputs_batch = inputs_no_trunc['input_ids'][0][chunk_start:chunk_end]  # get batch of n tokens
            inputs_batch = torch.unsqueeze(inputs_batch, 0)
            inputs_batch_lst.append(inputs_batch)
            chunk_start += MAX_LEN  # == 1024 for Bart
            chunk_end += MAX_LEN  # == 1024 for Bart

        #debug
        self.inputs_batch_lst = inputs_batch_lst

        # generate a summary on each batch
        summary_ids_lst = [self.model.generate(
            inputs, 
            num_beams=4, 
            max_length=80, 
            early_stopping=True
        ) for inputs in inputs_batch_lst]

        # decode the output and join into one string with one paragraph per summary batch
        summary_batch_lst = []
        for summary_id in summary_ids_lst:
            summary_batch = [self.tokenizer.decode(
                g, 
                skip_special_tokens=True, 
                clean_up_tokenization_spaces=False
            ) for g in summary_id]
            summary_batch_lst.append(summary_batch[0])
        summary_all = ' '.join(summary_batch_lst)

        return summary_all



