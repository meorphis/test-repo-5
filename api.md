# Accounts

Types:

```python
from meorphis_test_22.types import AccountRetrieveResponse, AccountUpdateResponse
```

Methods:

- <code title="get /accounts/{account_token}">client.accounts.<a href="./src/meorphis_test_22/resources/accounts/accounts.py">retrieve</a>(account_token) -> <a href="./src/meorphis_test_22/types/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="patch /accounts/{account_token}">client.accounts.<a href="./src/meorphis_test_22/resources/accounts/accounts.py">update</a>(account_token, \*\*<a href="src/meorphis_test_22/types/account_update_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/account_update_response.py">AccountUpdateResponse</a></code>

## CreditConfigurations

Types:

```python
from meorphis_test_22.types.accounts import (
    CreditConfigurationListResponse,
    CreditConfigurationPatchAccountCreditConfigurationResponse,
)
```

Methods:

- <code title="get /accounts/{account_token}/credit_configuration">client.accounts.credit_configurations.<a href="./src/meorphis_test_22/resources/accounts/credit_configurations.py">list</a>(account_token) -> <a href="./src/meorphis_test_22/types/accounts/credit_configuration_list_response.py">CreditConfigurationListResponse</a></code>
- <code title="patch /accounts/{account_token}/credit_configuration">client.accounts.credit_configurations.<a href="./src/meorphis_test_22/resources/accounts/credit_configurations.py">patch_account_credit_configuration</a>(account_token, \*\*<a href="src/meorphis_test_22/types/accounts/credit_configuration_patch_account_credit_configuration_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/accounts/credit_configuration_patch_account_credit_configuration_response.py">CreditConfigurationPatchAccountCreditConfigurationResponse</a></code>

# Cards

Types:

```python
from meorphis_test_22.types import CardCreateResponse, CardRetrieveResponse, CardUpdateResponse
```

Methods:

- <code title="post /cards">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">create</a>(\*\*<a href="src/meorphis_test_22/types/card_create_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/card_create_response.py">CardCreateResponse</a></code>
- <code title="get /cards/{card_token}">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">retrieve</a>(card_token) -> <a href="./src/meorphis_test_22/types/card_retrieve_response.py">CardRetrieveResponse</a></code>
- <code title="patch /cards/{card_token}">client.cards.<a href="./src/meorphis_test_22/resources/cards/cards.py">update</a>(card_token, \*\*<a href="src/meorphis_test_22/types/card_update_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/card_update_response.py">CardUpdateResponse</a></code>

## FinancialTransactions

Types:

```python
from meorphis_test_22.types.cards import FinancialTransactionGetFinancialTransactionByTokenResponse
```

Methods:

- <code title="get /cards/{card_token}/financial_transactions/{financial_transaction_token}">client.cards.financial_transactions.<a href="./src/meorphis_test_22/resources/cards/financial_transactions.py">get_financial_transaction_by_token</a>(financial_transaction_token, \*, card_token) -> <a href="./src/meorphis_test_22/types/cards/financial_transaction_get_financial_transaction_by_token_response.py">FinancialTransactionGetFinancialTransactionByTokenResponse</a></code>

## Provisions

Types:

```python
from meorphis_test_22.types.cards import ProvisionPostProvisionResponse
```

Methods:

- <code title="post /cards/{card_token}/provision">client.cards.provisions.<a href="./src/meorphis_test_22/resources/cards/provisions.py">post_provision</a>(card_token, \*\*<a href="src/meorphis_test_22/types/cards/provision_post_provision_params.py">params</a>) -> <a href="./src/meorphis_test_22/types/cards/provision_post_provision_response.py">ProvisionPostProvisionResponse</a></code>

# Statuses

Types:

```python
from meorphis_test_22.types import StatusGetStatusResponse
```

Methods:

- <code title="get /status">client.statuses.<a href="./src/meorphis_test_22/resources/statuses.py">get_status</a>() -> <a href="./src/meorphis_test_22/types/status_get_status_response.py">StatusGetStatusResponse</a></code>
