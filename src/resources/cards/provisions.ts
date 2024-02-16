// File generated from our OpenAPI spec by Stainless.

import * as Core from '/core';
import { APIResource } from '/resource';
import * as ProvisionsAPI from '/resources/cards/provisions';

export class Provisions extends APIResource {
  /**
   * Allow your cardholders to directly add payment cards to the device's digital
   * wallet (e.g. Apple Pay) with one touch from your app.
   *
   * This requires some additional setup and configuration. Please
   * [Contact Us](https://acme.com/contact) or your Customer Success representative
   * for more information.
   */
  postProvision(
    cardToken: string,
    params: ProvisionPostProvisionParams,
    options?: Core.RequestOptions,
  ): Core.APIPromise<ProvisionPostProvisionResponse> {
    const { 'Idempotency-Key': idempotencyKey, ...body } = params;
    return this._client.post(`/cards/${cardToken}/provision`, {
      body,
      ...options,
      headers: { 'Idempotency-Key': idempotencyKey || '', ...options?.headers },
    });
  }
}

export interface ProvisionPostProvisionResponse {
  provisioning_payload?: string;
}

export interface ProvisionPostProvisionParams {
  /**
   * Body param: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive
   * only `activationData` in the response. Apple's public leaf certificate. Base64
   * encoded in PEM format with headers `(-----BEGIN CERTIFICATE-----)` and trailers
   * omitted. Provided by the device's wallet.
   */
  certificate?: string;

  /**
   * Body param: Name of digital wallet provider.
   */
  digital_wallet?: 'APPLE_PAY' | 'GOOGLE_PAY' | 'SAMSUNG_PAY';

  /**
   * Body param: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive
   * only `activationData` in the response. Base64 cryptographic nonce provided by
   * the device's wallet.
   */
  nonce?: string;

  /**
   * Body param: Only applicable if `digital_wallet` is `APPLE_PAY`. Omit to receive
   * only `activationData` in the response. Base64 cryptographic nonce provided by
   * the device's wallet.
   */
  nonce_signature?: string;

  /**
   * Header param: Idempotency key for the POST request. See
   * [Idempotency Requests](https://docs.acme.com/docs/idempotent-requests) for
   * details on behavior such as cache duration.
   */
  'Idempotency-Key'?: string;
}

export namespace Provisions {
  export import ProvisionPostProvisionResponse = ProvisionsAPI.ProvisionPostProvisionResponse;
  export import ProvisionPostProvisionParams = ProvisionsAPI.ProvisionPostProvisionParams;
}
