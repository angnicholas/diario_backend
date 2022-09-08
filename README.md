# Diario Online Journal: Django Backend


### Instructions for setup
1. Install requirements with `pip3 install -r requirements.txt`
2. (Optionally) edit the DJANGO_SECRET_KEY variable in .env to a custom key created using `django-admin startproject`. This is for security during deployment, not necessary for local testing.
3. Migrate the database: 

```python manage.py migrate #Build database```

4. Load preset data:

```python manage.py load_fixtures```

OR

```python manage.py load_fixtures_DEMO #To pre-load data ```

5. Run the server

```python manage.py runserver```

### Users created when loading fixtures
If you called `load_fixtures`, the following user objects will be created (all passwords are `test1234!`)
<table>
    <tr>
        <td>Username</td>
        <td>Role</td>
        <td>Remarks</td>
    </tr>
    <tr>
        <td>t1</td>
        <td>Therapist</td>
        <td></td>
    </tr>
    <tr>
        <td>t2</td>
        <td>Therapist</td>
        <td></td>
    </tr>
    <tr>
        <td>p1</td>
        <td>Patient</td>
        <td>Attached to therapist t1</td>
    </tr>
    <tr>
        <td>p2</td>
        <td>Patient</td>
        <td>Attached to therapist t1</td>
    </tr>
    <tr>
        <td>p3</td>
        <td>Patient</td>
        <td>Attached to therapist t2</td>
    </tr>
</table>

If you called `load_fixtures_DEMO`, the following user objects will be created (all passwords are `test1234!`)
<table>
    <tr>
        <td>Username</td>
        <td>Role</td>
        <td>Remarks</td>
    </tr>
    <tr>
        <td>alex</td>
        <td>Therapist</td>
        <td></td>
    </tr>
    <tr>
        <td>ben</td>
        <td>Patient</td>
        <td>Attached to therapist alex</td>
    </tr>
    <tr>
        <td>charlie</td>
        <td>Patient</td>
        <td>Attached to therapist alex</td>
    </tr>
</table>