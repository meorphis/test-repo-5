# Accounts

Types:

- <code><a href="./src/resources/accounts/accounts.ts">AccountRetrieveResponse</a></code>
- <code><a href="./src/resources/accounts/accounts.ts">AccountUpdateResponse</a></code>

Methods:

- <code title="get /accounts/{account_token}">client.accounts.<a href="./src/resources/accounts/accounts.ts">retrieve</a>(accountToken) -> AccountRetrieveResponse</code>
- <code title="patch /accounts/{account_token}">client.accounts.<a href="./src/resources/accounts/accounts.ts">update</a>(accountToken, { ...params }) -> AccountUpdateResponse</code>

## CreditConfigurations

Types:

- <code><a href="./src/resources/accounts/credit-configurations.ts">CreditConfigurationListResponse</a></code>
- <code><a href="./src/resources/accounts/credit-configurations.ts">CreditConfigurationPatchAccountCreditConfigurationResponse</a></code>

Methods:

- <code title="get /accounts/{account_token}/credit_configuration">client.accounts.creditConfigurations.<a href="./src/resources/accounts/credit-configurations.ts">list</a>(accountToken) -> CreditConfigurationListResponse</code>
- <code title="patch /accounts/{account_token}/credit_configuration">client.accounts.creditConfigurations.<a href="./src/resources/accounts/credit-configurations.ts">patchAccountCreditConfiguration</a>(accountToken, { ...params }) -> CreditConfigurationPatchAccountCreditConfigurationResponse</code>

# Cards

Types:

- <code><a href="./src/resources/cards/cards.ts">CardCreateResponse</a></code>
- <code><a href="./src/resources/cards/cards.ts">CardRetrieveResponse</a></code>
- <code><a href="./src/resources/cards/cards.ts">CardUpdateResponse</a></code>

Methods:

- <code title="post /cards">client.cards.<a href="./src/resources/cards/cards.ts">create</a>({ ...params }) -> CardCreateResponse</code>
- <code title="get /cards/{card_token}">client.cards.<a href="./src/resources/cards/cards.ts">retrieve</a>(cardToken) -> CardRetrieveResponse</code>
- <code title="patch /cards/{card_token}">client.cards.<a href="./src/resources/cards/cards.ts">update</a>(cardToken, { ...params }) -> CardUpdateResponse</code>

## FinancialTransactions

Types:

- <code><a href="./src/resources/cards/financial-transactions.ts">FinancialTransactionGetFinancialTransactionByTokenResponse</a></code>

Methods:

- <code title="get /cards/{card_token}/financial_transactions/{financial_transaction_token}">client.cards.financialTransactions.<a href="./src/resources/cards/financial-transactions.ts">getFinancialTransactionByToken</a>(cardToken, financialTransactionToken) -> FinancialTransactionGetFinancialTransactionByTokenResponse</code>

## Provisions

Types:

- <code><a href="./src/resources/cards/provisions.ts">ProvisionPostProvisionResponse</a></code>

Methods:

- <code title="post /cards/{card_token}/provision">client.cards.provisions.<a href="./src/resources/cards/provisions.ts">postProvision</a>(cardToken, { ...params }) -> ProvisionPostProvisionResponse</code>

# Statuses

Types:

- <code><a href="./src/resources/statuses.ts">StatusGetStatusResponse</a></code>

Methods:

- <code title="get /status">client.statuses.<a href="./src/resources/statuses.ts">getStatus</a>() -> StatusGetStatusResponse</code>
