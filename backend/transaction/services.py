from transaction.models import Transaction, TransactionStatus
from transaction.utils import configure_paypal
from paypalrestsdk import Payment

from django.core.exceptions import ObjectDoesNotExist


def get_amount_received(party):
    """
    Amount received by party
    where party is payer or recipient
    """
    return Transaction.objects.amount_received(party)


def create_transaction(payer, recipient, amount, **extra_fields):
    """Create a transaction within the app."""
    return Transaction.objects.create_transaction(
        payer, recipient, amount, **extra_fields
    )


def create_paypal_transaction(
    payer, recipient, amount, return_url, cancel_url
):
    """Create a real-money transaction with PayPal"""
    configure_paypal()

    payment_data = {
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [
            {
                "amount": {
                    "total": f"{amount:.2f}",
                    "currency": "USD",
                },
                "description": "Payment transaction description",
            }
        ],
        "redirect_urls": {
            "return_url": return_url,
            "cancel_url": cancel_url,
        },
    }
    payment = Payment(payment_data)

    if payment.create():
        transaction = create_transaction(
            payer=payer,
            recipient=recipient,
            amount=amount,
            payment_id=payment.id,
            status=TransactionStatus.PENDING,
        )
        return payment, transaction
    else:
        raise Exception(payment.error)


def execute_paypal_transaction(payment_id, payer_id):
    """Execute a real-money transaction with PayPal"""
    configure_paypal()

    payment = Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        try:
            transaction = Transaction.objects.get(payment_id=payment_id)
            transaction.status = TransactionStatus.COMPLETED
            transaction.save()
        except ObjectDoesNotExist:
            raise ValueError("Transaction not found for the given payment ID.")

        return payment
    else:
        raise Exception(payment.error)
