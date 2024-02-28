# Accounts

Types:

```python
from meorphis_test_22.types import AccountConfiguration
```

Methods:

- <code title="get /accounts/{account_token}">client.accounts.<a href="./src/meorphis_test_22/resources/accounts/accounts.py">retrieve</a>(account_token) -> <a href="./src/meorphis_test_22/types/account_configuration.py">AccountConfiguration</a></code>
- <code title="patch /accounts/{account_token}">client.accounts.<a href="./src/meorphis_test_22/resources/accounts/accounts.py">update</a>(account_token, \*\*<a href="src/meorphis_test_22/types/account_update_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/account_configuration.py">AccountConfiguration</a></code>

## CreditConfiguration

Types:

```python
from meorphis_test_22.types.accounts import BusinessAccount
```

Methods:

- <code title="get /accounts/{account_token}/credit_configuration">client.accounts.credit_configuration.<a href="./src/meorphis_test_22/resources/accounts/credit_configuration.py">retrieve</a>(account_token) -> <a href="./src/meorphis_test_22/types/accounts/business_account.py">BusinessAccount</a></code>
- <code title="patch /accounts/{account_token}/credit_configuration">client.accounts.credit_configuration.<a href="./src/meorphis_test_22/resources/accounts/credit_configuration.py">update</a>(account_token, \*\*<a href="src/meorphis_test_22/types/accounts/credit_configuration_update_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/accounts/business_account.py">BusinessAccount</a></code>

# Cards

Types:

```python
from meorphis_test_22.types import Card, CardProvisionResponse
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">create</a>(\*\*<a href="src/meorphis_test_22/types/card_create_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/card.py">Card</a></code>
- <code title="get /cards/{card_token}">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">retrieve</a>(card_token) -> <a href="./src/meorphis_test_22/types/card.py">Card</a></code>
- <code title="patch /cards/{card_token}">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">update</a>(card_token, \*\*<a href="src/meorphis_test_22/types/card_update_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/card.py">Card</a></code>
- <code title="post /cards/{card_token}/provision">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">provision</a>(card_token, \*\*<a href="src/meorphis_test_22/types/card_provision_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/card_provision_response.py">CardProvisionResponse</a></code>

## FinancialTransactions

Types:

```python
from meorphis_test_22.types.cards import FinancialTransaction
```

Methods:

- <code title="get /cards/{card_token}/financial_transactions/{financial_transaction_token}">client.cards.financial_transactions.<a href="./src/meorphis_test_22/resources/cards/financial_transactions.py">retrieve</a>(financial_transaction_token, \*, card_token) -> <a href="./src/meorphis_test_22/types/cards/financial_transaction.py">FinancialTransaction</a></code>

# Status

Types:

```python
from meorphis_test_22.types import StatusRetrieveResponse
```

Methods:

- <code title="get /status">client.status.<a href="./src/meorphis_test_22/resources/status.py">retrieve</a>() -> <a href="./src/meorphis_test_22/types/status_retrieve_response.py">StatusRetrieveResponse</a></code>
