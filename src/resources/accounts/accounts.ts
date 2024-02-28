// File generated from our OpenAPI spec by Stainless.

import * as Core from 'meorphis-test-22/core';
import { APIResource } from 'meorphis-test-22/resource';
import * as AccountsAPI from 'meorphis-test-22/resources/accounts/accounts';
import * as CreditConfigurationsAPI from 'meorphis-test-22/resources/accounts/credit-configurations';

export class Accounts extends APIResource {
  creditConfigurations: CreditConfigurationsAPI.CreditConfigurations =
    new CreditConfigurationsAPI.CreditConfigurations(this._client);

  /**
   * Get account configuration such as spend limits.
   */
  retrieve(accountToken: string, options?: Core.RequestOptions): Core.APIPromise<AccountRetrieveResponse> {
    return this._client.get(`/accounts/${accountToken}`, options);
  }

  /**
   * Update account configuration such as spend limits and verification address. Can
   * only be run on accounts that are part of the program managed by this API key.
   *
   * Accounts that are in the `PAUSED` state will not be able to transact or create
   * new cards.
   */
  update(
    accountToken: string,
    body: AccountUpdateParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<AccountUpdateResponse> {
    return this._client.patch(`/accounts/${accountToken}`, { body, ...options });
  }
}

export interface AccountRetrieveResponse {
  /**
   * Globally unique identifier for the account. This is the same as the
   * account_token returned by the enroll endpoint. If using this parameter, do not
   * include pagination.
   */
  token: string;

  /**
   * Spend limit information for the user containing the daily, monthly, and lifetime
   * spend limit of the account. Any charges to a card owned by this account will be
   * declined once their transaction volume has surpassed the value in the applicable
   * time limit (rolling). A lifetime limit of 0 indicates that the lifetime limit
   * feature is disabled.
   */
  spend_limit: AccountRetrieveResponse.SpendLimit;

  /**
   * Account state:
   *
   * - `ACTIVE` - Account is able to transact and create new cards.
   * - `PAUSED` - Account will not be able to transact or create new cards. It can be
   *   set back to `ACTIVE`.
   * - `CLOSED` - Account will permanently not be able to transact or create new
   *   cards.
   */
  state: 'ACTIVE' | 'PAUSED' | 'CLOSED';

  account_holder?: AccountRetrieveResponse.AccountHolder;

  /**
   * List of identifiers for the Auth Rule(s) that are applied on the account.
   */
  auth_rule_tokens?: Array<string>;

  verification_address?: AccountRetrieveResponse.VerificationAddress;
}

export namespace AccountRetrieveResponse {
  /**
   * Spend limit information for the user containing the daily, monthly, and lifetime
   * spend limit of the account. Any charges to a card owned by this account will be
   * declined once their transaction volume has surpassed the value in the applicable
   * time limit (rolling). A lifetime limit of 0 indicates that the lifetime limit
   * feature is disabled.
   */
  export interface SpendLimit {
    /**
     * Daily spend limit (in cents).
     */
    daily: number;

    /**
     * Total spend limit over account lifetime (in cents).
     */
    lifetime: number;

    /**
     * Monthly spend limit (in cents).
     */
    monthly: number;
  }

  export interface AccountHolder {
    /**
     * Globally unique identifier for the account holder.
     */
    token: string;

    /**
     * Only applicable for customers using the KYC-Exempt workflow to enroll authorized
     * users of businesses. Account_token of the enrolled business associated with an
     * enrolled AUTHORIZED_USER individual.
     */
    business_account_token: string;

    /**
     * Email address.
     */
    email: string;

    /**
     * Phone number of the individual.
     */
    phone_number: string;
  }

  export interface VerificationAddress {
    /**
     * Valid deliverable address (no PO boxes).
     */
    address1: string;

    /**
     * City name.
     */
    city: string;

    /**
     * Country name. Only USA is currently supported.
     */
    country: string;

    /**
     * Valid postal code. Only USA ZIP codes are currently supported, entered as a
     * five-digit ZIP or nine-digit ZIP+4.
     */
    postal_code: string;

    /**
     * Valid state code. Only USA state codes are currently supported, entered in
     * uppercase ISO 3166-2 two-character format.
     */
    state: string;

    /**
     * Unit or apartment number (if applicable).
     */
    address2?: string;
  }
}

export interface AccountUpdateResponse {
  /**
   * Globally unique identifier for the account. This is the same as the
   * account_token returned by the enroll endpoint. If using this parameter, do not
   * include pagination.
   */
  token: string;

  /**
   * Spend limit information for the user containing the daily, monthly, and lifetime
   * spend limit of the account. Any charges to a card owned by this account will be
   * declined once their transaction volume has surpassed the value in the applicable
   * time limit (rolling). A lifetime limit of 0 indicates that the lifetime limit
   * feature is disabled.
   */
  spend_limit: AccountUpdateResponse.SpendLimit;

  /**
   * Account state:
   *
   * - `ACTIVE` - Account is able to transact and create new cards.
   * - `PAUSED` - Account will not be able to transact or create new cards. It can be
   *   set back to `ACTIVE`.
   * - `CLOSED` - Account will permanently not be able to transact or create new
   *   cards.
   */
  state: 'ACTIVE' | 'PAUSED' | 'CLOSED';

  account_holder?: AccountUpdateResponse.AccountHolder;

  /**
   * List of identifiers for the Auth Rule(s) that are applied on the account.
   */
  auth_rule_tokens?: Array<string>;

  verification_address?: AccountUpdateResponse.VerificationAddress;
}

export namespace AccountUpdateResponse {
  /**
   * Spend limit information for the user containing the daily, monthly, and lifetime
   * spend limit of the account. Any charges to a card owned by this account will be
   * declined once their transaction volume has surpassed the value in the applicable
   * time limit (rolling). A lifetime limit of 0 indicates that the lifetime limit
   * feature is disabled.
   */
  export interface SpendLimit {
    /**
     * Daily spend limit (in cents).
     */
    daily: number;

    /**
     * Total spend limit over account lifetime (in cents).
     */
    lifetime: number;

    /**
     * Monthly spend limit (in cents).
     */
    monthly: number;
  }

  export interface AccountHolder {
    /**
     * Globally unique identifier for the account holder.
     */
    token: string;

    /**
     * Only applicable for customers using the KYC-Exempt workflow to enroll authorized
     * users of businesses. Account_token of the enrolled business associated with an
     * enrolled AUTHORIZED_USER individual.
     */
    business_account_token: string;

    /**
     * Email address.
     */
    email: string;

    /**
     * Phone number of the individual.
     */
    phone_number: string;
  }

  export interface VerificationAddress {
    /**
     * Valid deliverable address (no PO boxes).
     */
    address1: string;

    /**
     * City name.
     */
    city: string;

    /**
     * Country name. Only USA is currently supported.
     */
    country: string;

    /**
     * Valid postal code. Only USA ZIP codes are currently supported, entered as a
     * five-digit ZIP or nine-digit ZIP+4.
     */
    postal_code: string;

    /**
     * Valid state code. Only USA state codes are currently supported, entered in
     * uppercase ISO 3166-2 two-character format.
     */
    state: string;

    /**
     * Unit or apartment number (if applicable).
     */
    address2?: string;
  }
}

export interface AccountUpdateParams {
  /**
   * Amount (in cents) for the account's daily spend limit. By default the daily
   * spend limit is set to $1,250.
   */
  daily_spend_limit?: number;

  /**
   * Amount (in cents) for the account's lifetime spend limit. Once this limit is
   * reached, no transactions will be accepted on any card created for this account
   * until the limit is updated. Note that a spend limit of 0 is effectively no
   * limit, and should only be used to reset or remove a prior limit. Only a limit of
   * 1 or above will result in declined transactions due to checks against the
   * account limit. This behavior differs from the daily spend limit and the monthly
   * spend limit.
   */
  lifetime_spend_limit?: number;

  /**
   * Amount (in cents) for the account's monthly spend limit. By default the monthly
   * spend limit is set to $5,000.
   */
  monthly_spend_limit?: number;

  /**
   * Account states.
   */
  state?: 'ACTIVE' | 'PAUSED';

  /**
   * Address used during Address Verification Service (AVS) checks during
   * transactions if enabled via Auth Rules.
   */
  verification_address?: AccountUpdateParams.VerificationAddress;
}

export namespace AccountUpdateParams {
  /**
   * Address used during Address Verification Service (AVS) checks during
   * transactions if enabled via Auth Rules.
   */
  export interface VerificationAddress {
    address1?: string;

    address2?: string;

    city?: string;

    country?: string;

    postal_code?: string;

    state?: string;
  }
}

export namespace Accounts {
  export import AccountRetrieveResponse = AccountsAPI.AccountRetrieveResponse;
  export import AccountUpdateResponse = AccountsAPI.AccountUpdateResponse;
  export import AccountUpdateParams = AccountsAPI.AccountUpdateParams;
  export import CreditConfigurations = CreditConfigurationsAPI.CreditConfigurations;
  export import CreditConfigurationListResponse = CreditConfigurationsAPI.CreditConfigurationListResponse;
  export import CreditConfigurationPatchAccountCreditConfigurationResponse = CreditConfigurationsAPI.CreditConfigurationPatchAccountCreditConfigurationResponse;
  export import CreditConfigurationPatchAccountCreditConfigurationParams = CreditConfigurationsAPI.CreditConfigurationPatchAccountCreditConfigurationParams;
}
