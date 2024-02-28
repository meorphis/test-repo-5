# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CardCreateParams", "Carrier", "ShippingAddress"]


class CardCreateParams(TypedDict, total=False):
    type: Required[Literal["VIRTUAL", "PHYSICAL", "MERCHANT_LOCKED", "SINGLE_USE"]]
    """Card types:

    - `VIRTUAL` - Card will authorize at any merchant and can be added to a digital
      wallet like Apple Pay or Google Pay (if the card program is digital
      wallet-enabled).
    - `PHYSICAL` - Manufactured and sent to the cardholder. We offer white label
      branding, credit, ATM, PIN debit, chip/EMV, NFC and magstripe functionality.
      Reach out at [acme.com/contact](https://acme.com/contact) for more
      information.
    - `SINGLE_USE` - Card is closed upon first successful authorization.
    - `MERCHANT_LOCKED` - _[Deprecated]_ Card is locked to the first merchant that
      successfully authorizes the card.
    """

    account_token: str
    """Globally unique identifier for the account that the card will be associated
    with.

    Required for programs enrolling users using the
    [/account_holders endpoint](https://docs.acme.com/docs/account-holders-kyc). See
    [Managing Your Program](doc:managing-your-program) for more information.
    """

    card_program_token: str
    """For card programs with more than one BIN range.

    This must be configured with Acme before use. Identifies the card program/BIN
    range under which to create the card. If omitted, will utilize the program's
    default `card_program_token`. In Sandbox, use
    00000000-0000-0000-1000-000000000000 and 00000000-0000-0000-2000-000000000000 to
    test creating cards on specific card programs.
    """

    carrier: Carrier

    digital_card_art_token: str
    """
    Specifies the digital card art to be displayed in the user’s digital wallet
    after tokenization. This artwork must be approved by Mastercard and configured
    by Acme to use. See
    [Flexible Card Art Guide](https://docs.acme.com/docs/about-digital-wallets#flexible-card-art).
    """

    exp_month: str
    """Two digit (MM) expiry month.

    If neither `exp_month` nor `exp_year` is provided, an expiration date will be
    generated.
    """

    exp_year: str
    """Four digit (yyyy) expiry year.

    If neither `exp_month` nor `exp_year` is provided, an expiration date will be
    generated.
    """

    memo: str
    """Friendly name to identify the card.

    We recommend against using this field to store JSON data as it can cause
    unexpected behavior.
    """

    pin: str
    """Encrypted PIN block (in base64).

    Only applies to cards of type `PHYSICAL` and `VIRTUAL`. See
    [Encrypted PIN Block](https://docs.acme.com/docs/cards#encrypted-pin-block-enterprise).
    """

    product_id: str
    """Only applicable to cards of type `PHYSICAL`.

    This must be configured with Acme before use. Specifies the configuration (i.e.,
    physical card art) that the card should be manufactured with.
    """

    shipping_address: ShippingAddress

    shipping_method: Literal["STANDARD", "STANDARD_WITH_TRACKING", "PRIORITY", "EXPRESS", "2_DAY", "EXPEDITED"]
    """Shipping method for the card.

    Only applies to cards of type PHYSICAL. Use of options besides `STANDARD`
    require additional permissions.

    - `STANDARD` - USPS regular mail or similar international option, with no
      tracking
    - `STANDARD_WITH_TRACKING` - USPS regular mail or similar international option,
      with tracking
    - `PRIORITY` - USPS Priority, 1-3 day shipping, with tracking
    - `EXPRESS` - FedEx Express, 3-day shipping, with tracking
    - `2_DAY` - FedEx 2-day shipping, with tracking
    - `EXPEDITED` - FedEx Standard Overnight or similar international option, with
      tracking
    """

    spend_limit: int
    """Amount (in cents) to limit approved authorizations.

    Transaction requests above the spend limit will be declined. Note that a spend
    limit of 0 is effectively no limit, and should only be used to reset or remove a
    prior limit. Only a limit of 1 or above will result in declined transactions due
    to checks against the card limit.
    """

    spend_limit_duration: Literal["ANNUALLY", "FOREVER", "MONTHLY", "TRANSACTION"]
    """Spend limit duration values:

    - `ANNUALLY` - Card will authorize transactions up to spend limit in a calendar
      year.
    - `FOREVER` - Card will authorize only up to spend limit for the entire lifetime
      of the card.
    - `MONTHLY` - Card will authorize transactions up to spend limit for the
      trailing month. Month is calculated as this calendar date one month prior.
    - `TRANSACTION` - Card will authorize multiple transactions if each individual
      transaction is under the spend limit.
    """

    state: Literal["OPEN", "PAUSED"]
    """Card state values:

    - `OPEN` - Card will approve authorizations (if they match card and account
      parameters).
    - `PAUSED` - Card will decline authorizations, but can be resumed at a later
      time.
    """


class Carrier(TypedDict, total=False):
    qr_code_url: str
    """QR code url to display on the card carrier"""


class ShippingAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid USPS routable address."""

    city: Required[str]
    """City"""

    country: Required[str]
    """Uppercase ISO 3166-1 alpha-3 three character abbreviation."""

    first_name: Required[str]
    """Customer's first name.

    This will be the first name printed on the physical card.
    """

    last_name: Required[str]
    """Customer's surname (family name).

    This will be the last name printed on the physical card.
    """

    postal_code: Required[str]
    """Postal code (formerly zipcode).

    For US addresses, either five-digit zipcode or nine-digit "ZIP+4".
    """

    state: Required[str]
    """Uppercase ISO 3166-2 two character abbreviation for US and CA.

    Optional with a limit of 24 characters for other countries.
    """

    address2: str
    """Unit number (if applicable)."""

    email: str
    """Email address to be contacted for expedited shipping process purposes.

    Required if `shipping_method` is `EXPEDITED`.
    """

    line2_text: str
    """Text to be printed on line two of the physical card.

    Use of this field requires additional permissions.
    """

    phone_number: str
    """
    Cardholder's phone number in E.164 format to be contacted for expedited shipping
    process purposes. Required if `shipping_method` is `EXPEDITED`.
    """
