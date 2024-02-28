// File generated from our OpenAPI spec by Stainless.

import * as Core from 'meorphis-test-22/core';
import { APIResource } from 'meorphis-test-22/resource';
import { isRequestOptions } from 'meorphis-test-22/core';
import * as CreditConfigurationsAPI from 'meorphis-test-22/resources/accounts/credit-configurations';

export class CreditConfigurations extends APIResource {
  /**
   * Get an Account's credit configuration
   */
  list(
    accountToken: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CreditConfigurationListResponse> {
    return this._client.get(`/accounts/${accountToken}/credit_configuration`, options);
  }

  /**
   * Update a Business Accounts credit configuration
   */
  patchAccountCreditConfiguration(
    accountToken: string,
    body?: CreditConfigurationPatchAccountCreditConfigurationParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CreditConfigurationPatchAccountCreditConfigurationResponse>;
  patchAccountCreditConfiguration(
    accountToken: string,
    options?: Core.RequestOptions,
  ): Core.APIPromise<CreditConfigurationPatchAccountCreditConfigurationResponse>;
  patchAccountCreditConfiguration(
    accountToken: string,
    body: CreditConfigurationPatchAccountCreditConfigurationParams | Core.RequestOptions = {},
    options?: Core.RequestOptions,
  ): Core.APIPromise<CreditConfigurationPatchAccountCreditConfigurationResponse> {
    if (isRequestOptions(body)) {
      return this.patchAccountCreditConfiguration(accountToken, {}, body);
    }
    return this._client.patch(`/accounts/${accountToken}/credit_configuration`, { body, ...options });
  }
}

export interface CreditConfigurationListResponse {
  /**
   * Account token
   */
  token: string;

  collections_configuration?: CreditConfigurationListResponse.CollectionsConfiguration;

  /**
   * Credit limit extended to the Account
   */
  credit_limit?: number;
}

export namespace CreditConfigurationListResponse {
  export interface CollectionsConfiguration {
    /**
     * Number of days within the billing period
     */
    billing_period: number;

    /**
     * Number of days after the billing period ends that a payment is required
     */
    payment_period: number;

    /**
     * The external bank account token to use for auto-collections
     */
    external_bank_account_token?: string;
  }
}

export interface CreditConfigurationPatchAccountCreditConfigurationResponse {
  /**
   * Account token
   */
  token: string;

  collections_configuration?: CreditConfigurationPatchAccountCreditConfigurationResponse.CollectionsConfiguration;

  /**
   * Credit limit extended to the Account
   */
  credit_limit?: number;
}

export namespace CreditConfigurationPatchAccountCreditConfigurationResponse {
  export interface CollectionsConfiguration {
    /**
     * Number of days within the billing period
     */
    billing_period: number;

    /**
     * Number of days after the billing period ends that a payment is required
     */
    payment_period: number;

    /**
     * The external bank account token to use for auto-collections
     */
    external_bank_account_token?: string;
  }
}

export interface CreditConfigurationPatchAccountCreditConfigurationParams {
  /**
   * Number of days within the billing period
   */
  billing_period?: number;

  /**
   * Credit limit extended to the Business Account
   */
  credit_limit?: number;

  /**
   * The external bank account token to use for auto-collections
   */
  external_bank_account_token?: string;

  /**
   * Number of days after the billing period ends that a payment is required
   */
  payment_period?: number;
}

export namespace CreditConfigurations {
  export import CreditConfigurationListResponse = CreditConfigurationsAPI.CreditConfigurationListResponse;
  export import CreditConfigurationPatchAccountCreditConfigurationResponse = CreditConfigurationsAPI.CreditConfigurationPatchAccountCreditConfigurationResponse;
  export import CreditConfigurationPatchAccountCreditConfigurationParams = CreditConfigurationsAPI.CreditConfigurationPatchAccountCreditConfigurationParams;
}
