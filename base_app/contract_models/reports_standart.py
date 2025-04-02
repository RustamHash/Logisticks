import pandas as pd

from ut.models import Invoice, Agent, InvoiceBody, Goods


def billing_tls(**kwargs):
    contract = kwargs['contract']
    start_date = kwargs['start_date']
    end_date = kwargs['end_date']
    prog_id = contract.filial.prog_id
    id_agent = contract.id_agent

    object_list = Invoice.objects.select_related().filter(
        program_id=prog_id,
        date_doc__range=(start_date, end_date),
        invoice_type_id=203,
        agent_id=id_agent,
        delivery=True
    )
    # columns = [field.verbose_name for field in object_list.model._meta.get_fields()],
    _col = ["ИД", "Дата",	"№ заказа",	"Довоз/Эксп", "Кому", "Адрес доставки",	"Масса нетто"]
    list_data = []
    for invoice in object_list:
        id_invoice = invoice.id
        date_doc = invoice.date_doc
        order_number = invoice.order_number
        agent_dovoz_id = Agent.objects.get(id=invoice.to_id.agent_dovoz_id).item_name
        item_name = invoice.to_id.item_name
        address = invoice.to_id.address
        list_data.append(list([id_invoice, date_doc, order_number, agent_dovoz_id, item_name, address, address]))
    df = pd.DataFrame(data=list_data, columns=_col)
    df['Дата'] = pd.to_datetime(df['Дата']).dt.date
    df.to_excel("reports_standart.xlsx", index=False)
