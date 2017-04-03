# OpenERP / Odoo - Project Issue Basic Dashboard

This is a full Django application, this will need to be changed, if you want to import this as an application

  - Two basic pages
    - Index.html - Overall view of agents / users and issues currently open
    - Index2.html - Lists of tickets in their current stage

# Setup

Requirements used in project:
(May not be necessary to run!)

| Library | Version |
|---------|---------|
| Django | 1.9.12 |
| django-pgfields | 1.4.4 |
| django-postgres-pgfields | 0.0.3 |
| django-postgresql | 0.0.3 |
| psycopg2 | 2.7.1 |
| pscopg2-managed-connection | 1.0.0 |
| six | 1.10.0 |
| wsgiref | 0.1.2 |

Install the relevant software required and run either using gunicorn/Apache with WSGI or simple python manage.py runserver to test.

# views.py

### For user information

This needs adjusting to pull in the relevant users you want to view in *index.html*, for example:

 `inprogress_user1 = inprogress_by_user.objects.filter(user='User1')` change to
 `inprogress_user1 = inprogress_by_user.objects.filter(user='jobloggs')`

For user jobloggs to appear in Dashboard.

### For the types of stages used

You need for each stage to add in a line and pass it to the `render_to_response`:

Add in each like the below:
`listofnew = ticket_by_stage.objects.filter(stage='New')`

Then in `render_to_response`:
`'listofnew': listofnew`
For each value to be passed to the templates, for each stage you would like to monitor.

# index.html

This shows current tickets by stage and users working on tickets, by user a stage called "In Progress". "Inp Progress" can be changed in views.py and this file for the template tags, to show represent the stage used to show the user is working on the ticket.

Ensure `<div class="ui five cards">` is adjusted, to the number of Semantic UI cards required to represent your data. If you require eight, then simple adjust `<div class="ui five cards">` to `<div class="ui eight cards">`.

For each `<div class="card">`, change the header text under `<div class="header">`
Under each card there is a `<div class="ui labels">` div tag, change the user name portion of the `{% %}` tag
Under each card there is a `<div class="ui large statistic">` div tag, change the loop for the ticket number the user is working on.

# index2.html
(Well named second template!)

This lists all issue ID's, named tickets in this version by stage type. What stages are used can be adjusted under views and then templates tags in this file, to show the relevant stages.

Ensure `<div class="ui five cards">` is adjusted, to the number of Semantic UI cards required to represent your data. If you require eight, then simple adjust `<div class="ui five cards">` to `<div class="ui eight cards">`.

For each `<div class="card">`, change or add the `{% %}` loops to represent the stage of the stages you would like to show.
