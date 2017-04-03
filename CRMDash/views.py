from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render_to_response
from .models import inprogress_by_user
from .models import calls_by_status
from .models import ticket_by_stage

# Create your views here.


def index(request):
    context = RequestContext(request)

    opencalls = calls_by_status.objects.filter(stage='Open')
    newcalls = calls_by_status.objects.filter(stage='New')
    awaitingcustomercalls = calls_by_status.objects.filter(stage='Awaiting Customer')
    inprogresscalls = calls_by_status.objects.filter(stage='In Progress')
    releasedcalls = calls_by_status.objects.filter(stage='Released')

    # TODO Add in the users you require to monitor or view. Use their Odoo username to identify them in the query below.
    # If you add in any additional users, make sure the template has been adjusted. Semantic-ui cards are used for each user

    inprogress_user1 = inprogress_by_user.objects.filter(user='User1')
    inprogress_user2 = inprogress_by_user.objects.filter(user='User2')
    inprogress_user3 = inprogress_by_user.objects.filter(user='User3')
    inprogress_user4 = inprogress_by_user.objects.filter(user='User4')
    inprogress_user5 = inprogress_by_user.objects.filter(user='User5')
    inprogress_user6 = inprogress_by_user.objects.filter(user='User6')
    inprogress_user7 = inprogress_by_user.objects.filter(user='User7')

    listofnew = ticket_by_stage.objects.filter(stage='New')
    listofopen = ticket_by_stage.objects.filter(stage='Open')
    listofawaitingcustomer = ticket_by_stage.objects.filter(stage='Awaiting Customer')
    listofinprogress = ticket_by_stage.objects.filter(stage='In Progress')

    # TODO remove or add in the required variables for your users, to be sent to the template.

    return render_to_response('index.html', {'inprogress_user1': inprogress_user1, 'inprogress_user2': inprogress_user2,
                                             'inprogress_user3': inprogress_user3, 'inprogress_user4': inprogress_user4,
                                             'inprogress_uesr5': inprogress_user5, 'inprogress_user6': inprogress_user6,
                                             'inprogress_user7': inprogress_user7,
                                             'opencalls': opencalls, 'newcalls': newcalls,
                                             'awaitingcustomercalls': awaitingcustomercalls,
                                             'inprogresscalls': inprogresscalls, 'listofnew': listofnew,
                                             'listofopen': listofopen, 'listofawaitingcustomer': listofawaitingcustomer,
                                             'listofinprogress': listofinprogress, 'releasedcalls': releasedcalls},
                              context)


def index2(request):
    context = RequestContext(request)

    # TODO Remove ALL unneccessary querys for this view, as many of these queries are redundant for this page and create unneccessary queries back to the database.

    opencalls = calls_by_status.objects.filter(stage='Open')
    newcalls = calls_by_status.objects.filter(stage='New')
    awaitingcustomercalls = calls_by_status.objects.filter(stage='Awaiting Customer')
    inprogresscalls = calls_by_status.objects.filter(stage='In Progress')
    releasedcalls = calls_by_status.objects.filter(stage='Released')

    # TODO Add in the users you require to monitor or view. Use their Odoo username to identify them in the query below.
    # If you add in any additional users, make sure the template has been adjusted. Semantic-ui cards are used for each user

    inprogress_user1 = inprogress_by_user.objects.filter(user='User1')
    inprogress_user2 = inprogress_by_user.objects.filter(user='User2')
    inprogress_user3 = inprogress_by_user.objects.filter(user='User3')
    inprogress_user4 = inprogress_by_user.objects.filter(user='User4')
    inprogress_user5 = inprogress_by_user.objects.filter(user='User5')
    inprogress_user6 = inprogress_by_user.objects.filter(user='User6')
    inprogress_user7 = inprogress_by_user.objects.filter(user='User7')

    listofnew = ticket_by_stage.objects.filter(stage='New')
    listofopen = ticket_by_stage.objects.filter(stage='Open')
    listofawaitingcustomer = ticket_by_stage.objects.filter(stage='Awaiting Customer')
    listofinprogress = ticket_by_stage.objects.filter(stage='In Progress')

    # TODO remove or add in the required variables for your users, to be sent to the template.

    return render_to_response('index2.html', {'inprogress_user1': inprogress_user1, 'inprogress_user2': inprogress_user2,
                                             'inprogress_user3': inprogress_user3, 'inprogress_user4': inprogress_user4,
                                             'inprogress_uesr5': inprogress_user5, 'inprogress_user6': inprogress_user6,
                                             'inprogress_user7': inprogress_user7,
                                             'opencalls': opencalls, 'newcalls': newcalls,
                                             'awaitingcustomercalls': awaitingcustomercalls,
                                             'inprogresscalls': inprogresscalls, 'listofnew': listofnew,
                                             'listofopen': listofopen, 'listofawaitingcustomer': listofawaitingcustomer,
                                             'listofinprogress': listofinprogress, 'releasedcalls': releasedcalls},
                              context)
