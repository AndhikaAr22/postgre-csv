def customer():
    return"""
    select * from customer
    """

def mix_table():
    return"""
    select
	h.transactiondate ,
	c.customername ,
	i.itemname ,
	i.price ,
	h.paymenttype 
    from customer c
    join headerselltransaction h on c.customerid  = h.customerid 
    join detailselltransaction d on d.transactionid = h.transactionid 
    join item i on i.itemid = d.itemid 

    """