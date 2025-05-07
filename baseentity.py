from enum import Enum
from typing import Optional, List, Any, Dict
from datetime import datetime


class AllScreenParts:
    pass

    def __init__(self, ) -> None:
        pass


class BaseEntity:
    filer_id: int
    user_id: int
    created_by: int
    ip_address: None
    modified_by: int
    modified_ip_address: None

    def __init__(self, filer_id: int, user_id: int, created_by: int, ip_address: None, modified_by: int, modified_ip_address: None) -> None:
        self.filer_id = filer_id
        self.user_id = user_id
        self.created_by = created_by
        self.ip_address = ip_address
        self.modified_by = modified_by
        self.modified_ip_address = modified_ip_address


class Country(Enum):
    EMPTY = ""
    USA = "USA"


class CountryName(Enum):
    EMPTY = ""
    UNITED_STATES = "UNITED STATES"


class State(Enum):
    EMPTY = ""
    WA = "WA"


class Address:
    attention: None
    notification_attention: None
    correspondence_email_address: None
    consolidation_correspondence_email_address: None
    zip_extension: None
    address_entity_type: None
    is_address_same: bool
    is_user_non_commercial_registered_agent: bool
    base_entity: BaseEntity
    is_invalid_state: bool
    is_agent_in_wa: None
    is_ra_street_address_valid: bool
    is_address_returned_mail: bool
    full_address: str
    id: int
    street_address1: Optional[str]
    street_address2: Optional[str]
    city: Optional[str]
    state: Optional[State]
    other_state: Optional[str]
    country: Optional[Country]
    zip5: Optional[str]
    zip4: Optional[str]
    postal_code: Optional[str]
    county: None
    county_name: None
    country_name: CountryName

    def __init__(self, attention: None, notification_attention: None, correspondence_email_address: None, consolidation_correspondence_email_address: None, zip_extension: None, address_entity_type: None, is_address_same: bool, is_user_non_commercial_registered_agent: bool, base_entity: BaseEntity, is_invalid_state: bool, is_agent_in_wa: None, is_ra_street_address_valid: bool, is_address_returned_mail: bool, full_address: str, id: int, street_address1: Optional[str], street_address2: Optional[str], city: Optional[str], state: Optional[State], other_state: Optional[str], country: Optional[Country], zip5: Optional[str], zip4: Optional[str], postal_code: Optional[str], county: None, county_name: None, country_name: CountryName) -> None:
        self.attention = attention
        self.notification_attention = notification_attention
        self.correspondence_email_address = correspondence_email_address
        self.consolidation_correspondence_email_address = consolidation_correspondence_email_address
        self.zip_extension = zip_extension
        self.address_entity_type = address_entity_type
        self.is_address_same = is_address_same
        self.is_user_non_commercial_registered_agent = is_user_non_commercial_registered_agent
        self.base_entity = base_entity
        self.is_invalid_state = is_invalid_state
        self.is_agent_in_wa = is_agent_in_wa
        self.is_ra_street_address_valid = is_ra_street_address_valid
        self.is_address_returned_mail = is_address_returned_mail
        self.full_address = full_address
        self.id = id
        self.street_address1 = street_address1
        self.street_address2 = street_address2
        self.city = city
        self.state = state
        self.other_state = other_state
        self.country = country
        self.zip5 = zip5
        self.zip4 = zip4
        self.postal_code = postal_code
        self.county = county
        self.county_name = county_name
        self.country_name = country_name


class BusinessInfoPrincipalOffice:
    principal_id: int
    sequence_no: int
    first_name: None
    last_name: None
    full_name: None
    title: None
    name: None
    middle_name: None
    phone_number: None
    email_address: None
    type_id: None
    principal_base_type: None
    principal_mailing_address: Address
    principal_street_address: Address
    is_same_as_mailing_address: bool
    is_same_as_agent_address: bool
    business_id: int
    status: None
    member_or_manager: int
    is_principal_office_not_in_wa: bool
    is_formation: bool
    is_not_required: bool
    is_acp: bool
    participant_number: None
    is_for_non_profit_amendment: bool
    is_old_data_exist: bool
    filer_id: int
    user_id: int
    created_by: int
    ip_address: None
    modified_by: int
    modified_ip_address: None

    def __init__(self, principal_id: int, sequence_no: int, first_name: None, last_name: None, full_name: None, title: None, name: None, middle_name: None, phone_number: None, email_address: None, type_id: None, principal_base_type: None, principal_mailing_address: Address, principal_street_address: Address, is_same_as_mailing_address: bool, is_same_as_agent_address: bool, business_id: int, status: None, member_or_manager: int, is_principal_office_not_in_wa: bool, is_formation: bool, is_not_required: bool, is_acp: bool, participant_number: None, is_for_non_profit_amendment: bool, is_old_data_exist: bool, filer_id: int, user_id: int, created_by: int, ip_address: None, modified_by: int, modified_ip_address: None) -> None:
        self.principal_id = principal_id
        self.sequence_no = sequence_no
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.title = title
        self.name = name
        self.middle_name = middle_name
        self.phone_number = phone_number
        self.email_address = email_address
        self.type_id = type_id
        self.principal_base_type = principal_base_type
        self.principal_mailing_address = principal_mailing_address
        self.principal_street_address = principal_street_address
        self.is_same_as_mailing_address = is_same_as_mailing_address
        self.is_same_as_agent_address = is_same_as_agent_address
        self.business_id = business_id
        self.status = status
        self.member_or_manager = member_or_manager
        self.is_principal_office_not_in_wa = is_principal_office_not_in_wa
        self.is_formation = is_formation
        self.is_not_required = is_not_required
        self.is_acp = is_acp
        self.participant_number = participant_number
        self.is_for_non_profit_amendment = is_for_non_profit_amendment
        self.is_old_data_exist = is_old_data_exist
        self.filer_id = filer_id
        self.user_id = user_id
        self.created_by = created_by
        self.ip_address = ip_address
        self.modified_by = modified_by
        self.modified_ip_address = modified_ip_address


class Criteria:
    id: None
    mulitiple_i_ds: None
    type: str
    business_type: None
    type_id: int
    page_id: int
    page_count: int
    total_row_count: int
    search_value: None
    search_entity_name: str
    is_search: bool
    search_criteria: None
    grand_total: float
    business_status_id: int
    business_type_id: int
    filing_type_id: None
    user_id: int
    agent_name: None
    principal_name: None
    agent_address: Address
    principal_address: Address
    start_date_of_incorporation: datetime
    end_date_of_incorporation: None
    expiration_date: None
    fields: None
    is_online: bool
    is_inhouse: bool
    search_type: str
    agent_id: int
    due_date: datetime
    modified_date: datetime
    filer_id: int
    is_success: bool
    filing_number: int
    percent_to_program_services: None
    ubi_number: None
    fein_no: None
    registration_number: int
    key_word_search: None
    entity_name: None
    charity_id: int
    fundraiser_id: int
    trust_id: int
    address1: None
    address2: None
    city: None
    county: int
    state: None
    zip5: None
    zip4: None
    zip: None
    officers: None
    address: None
    status: None
    organization_type: None
    renewal_date: datetime
    tax_exempt_status: int
    hotlist: None
    referred_to_ag: None
    notifications: None
    date_range_start_date: datetime
    date_range_end_date: datetime
    export: int
    inquiry_status: int
    trasaction_category: None
    is_optional_registration: bool
    advance_is_optional_registration: None
    inquiry_status_id: None
    sort_type: None
    sort_by: None
    cft_type: None
    trademark_goods_id: None
    trademark_services_id: None
    trademark_text: None
    trademark_owner_name: None
    trademark_registration_no: None
    document_type_id: int
    document_id: int
    is_advanced_search: bool
    is_host_home_search: None
    is_public_benefit_non_profit_search: None
    is_charitable_non_profit_search: None
    is_gross_revenue_non_profit_search: None
    is_has_members_search: None
    is_has_fein_search: None
    fein_no_search: None
    is_charitable_non_profit: bool
    cft_business_list: None

    def __init__(self, id: None, mulitiple_i_ds: None, type: str, business_type: None, type_id: int, page_id: int, page_count: int, total_row_count: int, search_value: None, search_entity_name: str, is_search: bool, search_criteria: None, grand_total: float, business_status_id: int, business_type_id: int, filing_type_id: None, user_id: int, agent_name: None, principal_name: None, agent_address: Address, principal_address: Address, start_date_of_incorporation: datetime, end_date_of_incorporation: None, expiration_date: None, fields: None, is_online: bool, is_inhouse: bool, search_type: str, agent_id: int, due_date: datetime, modified_date: datetime, filer_id: int, is_success: bool, filing_number: int, percent_to_program_services: None, ubi_number: None, fein_no: None, registration_number: int, key_word_search: None, entity_name: None, charity_id: int, fundraiser_id: int, trust_id: int, address1: None, address2: None, city: None, county: int, state: None, zip5: None, zip4: None, zip: None, officers: None, address: None, status: None, organization_type: None, renewal_date: datetime, tax_exempt_status: int, hotlist: None, referred_to_ag: None, notifications: None, date_range_start_date: datetime, date_range_end_date: datetime, export: int, inquiry_status: int, trasaction_category: None, is_optional_registration: bool, advance_is_optional_registration: None, inquiry_status_id: None, sort_type: None, sort_by: None, cft_type: None, trademark_goods_id: None, trademark_services_id: None, trademark_text: None, trademark_owner_name: None, trademark_registration_no: None, document_type_id: int, document_id: int, is_advanced_search: bool, is_host_home_search: None, is_public_benefit_non_profit_search: None, is_charitable_non_profit_search: None, is_gross_revenue_non_profit_search: None, is_has_members_search: None, is_has_fein_search: None, fein_no_search: None, is_charitable_non_profit: bool, cft_business_list: None) -> None:
        self.id = id
        self.mulitiple_i_ds = mulitiple_i_ds
        self.type = type
        self.business_type = business_type
        self.type_id = type_id
        self.page_id = page_id
        self.page_count = page_count
        self.total_row_count = total_row_count
        self.search_value = search_value
        self.search_entity_name = search_entity_name
        self.is_search = is_search
        self.search_criteria = search_criteria
        self.grand_total = grand_total
        self.business_status_id = business_status_id
        self.business_type_id = business_type_id
        self.filing_type_id = filing_type_id
        self.user_id = user_id
        self.agent_name = agent_name
        self.principal_name = principal_name
        self.agent_address = agent_address
        self.principal_address = principal_address
        self.start_date_of_incorporation = start_date_of_incorporation
        self.end_date_of_incorporation = end_date_of_incorporation
        self.expiration_date = expiration_date
        self.fields = fields
        self.is_online = is_online
        self.is_inhouse = is_inhouse
        self.search_type = search_type
        self.agent_id = agent_id
        self.due_date = due_date
        self.modified_date = modified_date
        self.filer_id = filer_id
        self.is_success = is_success
        self.filing_number = filing_number
        self.percent_to_program_services = percent_to_program_services
        self.ubi_number = ubi_number
        self.fein_no = fein_no
        self.registration_number = registration_number
        self.key_word_search = key_word_search
        self.entity_name = entity_name
        self.charity_id = charity_id
        self.fundraiser_id = fundraiser_id
        self.trust_id = trust_id
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.county = county
        self.state = state
        self.zip5 = zip5
        self.zip4 = zip4
        self.zip = zip
        self.officers = officers
        self.address = address
        self.status = status
        self.organization_type = organization_type
        self.renewal_date = renewal_date
        self.tax_exempt_status = tax_exempt_status
        self.hotlist = hotlist
        self.referred_to_ag = referred_to_ag
        self.notifications = notifications
        self.date_range_start_date = date_range_start_date
        self.date_range_end_date = date_range_end_date
        self.export = export
        self.inquiry_status = inquiry_status
        self.trasaction_category = trasaction_category
        self.is_optional_registration = is_optional_registration
        self.advance_is_optional_registration = advance_is_optional_registration
        self.inquiry_status_id = inquiry_status_id
        self.sort_type = sort_type
        self.sort_by = sort_by
        self.cft_type = cft_type
        self.trademark_goods_id = trademark_goods_id
        self.trademark_services_id = trademark_services_id
        self.trademark_text = trademark_text
        self.trademark_owner_name = trademark_owner_name
        self.trademark_registration_no = trademark_registration_no
        self.document_type_id = document_type_id
        self.document_id = document_id
        self.is_advanced_search = is_advanced_search
        self.is_host_home_search = is_host_home_search
        self.is_public_benefit_non_profit_search = is_public_benefit_non_profit_search
        self.is_charitable_non_profit_search = is_charitable_non_profit_search
        self.is_gross_revenue_non_profit_search = is_gross_revenue_non_profit_search
        self.is_has_members_search = is_has_members_search
        self.is_has_fein_search = is_has_fein_search
        self.fein_no_search = fein_no_search
        self.is_charitable_non_profit = is_charitable_non_profit
        self.cft_business_list = cft_business_list


class Agent:
    type: None
    agent_id: int
    entity_name: None
    organization_name: None
    first_name: None
    last_name: None
    is_non_commercial: bool
    email_address: None
    agent_type_id: int
    street_address: Address
    mailing_address: Address
    is_user_registered_agent: bool
    phone_number: None
    is_registered_agent_consent: bool
    title: None
    is_same_as_mailing_address: bool
    created_by: None
    agent_creatd_date: None
    agent_creatd_ip: None
    is_new_agent: bool
    total_count: int
    is_agent_consent_show: bool
    is_agent_change: bool
    is_agent_formation: bool
    office_or_position: None
    business_id_for_ra: int
    business_agent_address_id: int
    business_agent_mailing_address_id: int
    is_agent_edit: bool
    is_agent_altered: bool
    is_online_agent: bool
    criteria: None
    agent_street1: None
    agent_street2: None
    city: None
    state: None
    other_state: None
    postal_code: None
    country: None
    zip4: None
    zip5: None
    business_type_id: int
    business_type: None
    jurisdiction: int
    jurisdiction_desc: None
    jurisdiction_state: int
    jurisdiction_country: int
    jurisdiction_state_desc: None
    jurisdiction_country_desc: None
    jurisdiction_category: None
    is_cra_registration: bool
    is_cra_attestation: bool
    is_cra_notification: bool
    is_cra_statementof_changed: bool
    is_represented_attestation: bool
    old_entity_name: None
    old_first_name: None
    old_last_name: None
    is_street_state_mustbein_wa: bool
    is_mailing_state_mustbein_wa: bool
    is_ra_address_valid: bool
    is_amendment_agent_info_change: bool
    is_ra_officeor_position_search: bool
    full_name: str
    agent_type: None
    is_acp: bool
    participant_number: None

    def __init__(self, type: None, agent_id: int, entity_name: None, organization_name: None, first_name: None, last_name: None, is_non_commercial: bool, email_address: None, agent_type_id: int, street_address: Address, mailing_address: Address, is_user_registered_agent: bool, phone_number: None, is_registered_agent_consent: bool, title: None, is_same_as_mailing_address: bool, created_by: None, agent_creatd_date: None, agent_creatd_ip: None, is_new_agent: bool, total_count: int, is_agent_consent_show: bool, is_agent_change: bool, is_agent_formation: bool, office_or_position: None, business_id_for_ra: int, business_agent_address_id: int, business_agent_mailing_address_id: int, is_agent_edit: bool, is_agent_altered: bool, is_online_agent: bool, criteria: None, agent_street1: None, agent_street2: None, city: None, state: None, other_state: None, postal_code: None, country: None, zip4: None, zip5: None, business_type_id: int, business_type: None, jurisdiction: int, jurisdiction_desc: None, jurisdiction_state: int, jurisdiction_country: int, jurisdiction_state_desc: None, jurisdiction_country_desc: None, jurisdiction_category: None, is_cra_registration: bool, is_cra_attestation: bool, is_cra_notification: bool, is_cra_statementof_changed: bool, is_represented_attestation: bool, old_entity_name: None, old_first_name: None, old_last_name: None, is_street_state_mustbein_wa: bool, is_mailing_state_mustbein_wa: bool, is_ra_address_valid: bool, is_amendment_agent_info_change: bool, is_ra_officeor_position_search: bool, full_name: str, agent_type: None, is_acp: bool, participant_number: None) -> None:
        self.type = type
        self.agent_id = agent_id
        self.entity_name = entity_name
        self.organization_name = organization_name
        self.first_name = first_name
        self.last_name = last_name
        self.is_non_commercial = is_non_commercial
        self.email_address = email_address
        self.agent_type_id = agent_type_id
        self.street_address = street_address
        self.mailing_address = mailing_address
        self.is_user_registered_agent = is_user_registered_agent
        self.phone_number = phone_number
        self.is_registered_agent_consent = is_registered_agent_consent
        self.title = title
        self.is_same_as_mailing_address = is_same_as_mailing_address
        self.created_by = created_by
        self.agent_creatd_date = agent_creatd_date
        self.agent_creatd_ip = agent_creatd_ip
        self.is_new_agent = is_new_agent
        self.total_count = total_count
        self.is_agent_consent_show = is_agent_consent_show
        self.is_agent_change = is_agent_change
        self.is_agent_formation = is_agent_formation
        self.office_or_position = office_or_position
        self.business_id_for_ra = business_id_for_ra
        self.business_agent_address_id = business_agent_address_id
        self.business_agent_mailing_address_id = business_agent_mailing_address_id
        self.is_agent_edit = is_agent_edit
        self.is_agent_altered = is_agent_altered
        self.is_online_agent = is_online_agent
        self.criteria = criteria
        self.agent_street1 = agent_street1
        self.agent_street2 = agent_street2
        self.city = city
        self.state = state
        self.other_state = other_state
        self.postal_code = postal_code
        self.country = country
        self.zip4 = zip4
        self.zip5 = zip5
        self.business_type_id = business_type_id
        self.business_type = business_type
        self.jurisdiction = jurisdiction
        self.jurisdiction_desc = jurisdiction_desc
        self.jurisdiction_state = jurisdiction_state
        self.jurisdiction_country = jurisdiction_country
        self.jurisdiction_state_desc = jurisdiction_state_desc
        self.jurisdiction_country_desc = jurisdiction_country_desc
        self.jurisdiction_category = jurisdiction_category
        self.is_cra_registration = is_cra_registration
        self.is_cra_attestation = is_cra_attestation
        self.is_cra_notification = is_cra_notification
        self.is_cra_statementof_changed = is_cra_statementof_changed
        self.is_represented_attestation = is_represented_attestation
        self.old_entity_name = old_entity_name
        self.old_first_name = old_first_name
        self.old_last_name = old_last_name
        self.is_street_state_mustbein_wa = is_street_state_mustbein_wa
        self.is_mailing_state_mustbein_wa = is_mailing_state_mustbein_wa
        self.is_ra_address_valid = is_ra_address_valid
        self.is_amendment_agent_info_change = is_amendment_agent_info_change
        self.is_ra_officeor_position_search = is_ra_officeor_position_search
        self.full_name = full_name
        self.agent_type = agent_type
        self.is_acp = is_acp
        self.participant_number = participant_number


class UploadDocuments:
    file_name: None
    file_location: None
    temp_file_name: None
    temp_file_location: None
    document_type_id: int
    document_type: None
    business_id: int
    business_filing_document_id: int
    filing_no: int
    created_by: int
    status: None
    transaction_id: int
    upload_file_name: None
    is_public_visible: bool
    number_of_pages: int
    filing_date_time: datetime
    source: None
    user_name: None
    is_online: bool
    cart_id: int
    upload_document_id: int
    document_table: None
    document_id: int

    def __init__(self, file_name: None, file_location: None, temp_file_name: None, temp_file_location: None, document_type_id: int, document_type: None, business_id: int, business_filing_document_id: int, filing_no: int, created_by: int, status: None, transaction_id: int, upload_file_name: None, is_public_visible: bool, number_of_pages: int, filing_date_time: datetime, source: None, user_name: None, is_online: bool, cart_id: int, upload_document_id: int, document_table: None, document_id: int) -> None:
        self.file_name = file_name
        self.file_location = file_location
        self.temp_file_name = temp_file_name
        self.temp_file_location = temp_file_location
        self.document_type_id = document_type_id
        self.document_type = document_type
        self.business_id = business_id
        self.business_filing_document_id = business_filing_document_id
        self.filing_no = filing_no
        self.created_by = created_by
        self.status = status
        self.transaction_id = transaction_id
        self.upload_file_name = upload_file_name
        self.is_public_visible = is_public_visible
        self.number_of_pages = number_of_pages
        self.filing_date_time = filing_date_time
        self.source = source
        self.user_name = user_name
        self.is_online = is_online
        self.cart_id = cart_id
        self.upload_document_id = upload_document_id
        self.document_table = document_table
        self.document_id = document_id


class Welcome4Element:
    is_available: bool
    principal_office: BusinessInfoPrincipalOffice
    principal_office_in_wa: None
    agent: None
    principals_list: None
    principal_name: None
    search_criteria: None
    search_type: None
    search_type_text: None
    search_value: None
    search_entity_name: None
    start_date_of_incorporation: datetime
    end_date_of_incorporation: datetime
    expiration_date: datetime
    criteria: Optional[Criteria]
    grange_address: None
    meeting_place: None
    is_org_business_name: bool
    check_business_name: None
    plus_or_minus_order: int
    filtere_record_id: int
    modified_date: datetime
    dissolution_days: int
    id: int
    is_inhouse: bool
    fee_list: None
    ubi_status: None
    is_ubi_number: bool
    new_ubi_number: None
    is_show_advance_search: bool
    entity_name: None
    status: None
    type: None
    is_host_home_search: None
    is_public_benefit_non_profit_search: None
    is_charitable_non_profit_search: None
    is_gross_revenue_non_profit_search: None
    is_has_members_search: None
    is_has_fein_search: None
    fein_no_search: None
    is_host_home: None
    is_public_benefit_non_profit: None
    is_charitable_non_profit: None
    is_gross_revenue_non_profit: None
    is_has_members: None
    is_has_fein: None
    is_host_home_confirm: bool
    entity_types_with_screens: AllScreenParts
    all_screen_parts: AllScreenParts
    online_report_principal_list: None
    online_upload_documents_list: List[Any]
    upload_documents_list: List[Any]
    principal_member_list: List[Any]
    correspondence_address: Address
    online_report_agent: Agent
    trademark_owner_agent: Agent
    online_report_authorized_person: Dict[str, Optional[bool]]
    online_report_business_transaction: None
    ar_due_date: datetime
    created_date: datetime
    date_began_doing_business_in_wa: datetime
    date_of_adoption: datetime
    date_of_formation_in_home_jurisdiction: datetime
    date_of_incorporation: datetime
    dissolved_date: datetime
    effective_date: datetime
    expiration_date_review: datetime
    filing_date: datetime
    next_ar_due_date: datetime
    periodof_duration_date: datetime
    ra_expired_date: datetime
    reinstatement_dissolution_end_date: datetime
    renewal_date: datetime
    requalification_termination_end_date: datetime
    duration_expire_date: None
    in_active_date: None
    last_ar_filed_date: None
    name_reservation_expire_date: None
    periodof_duration_date_review: None
    online_report_nature_of_business: None
    online_cart_entity: None
    business_info_principal_office: BusinessInfoPrincipalOffice
    business_info_principal_office_in_wa: BusinessInfoPrincipalOffice
    online_report_principal_office: BusinessInfoPrincipalOffice
    upload_documents: UploadDocuments
    osos_corp_signature_block_email: None
    osos_corp_email_signature: None
    osos_corp_email_signature_no_email: None
    osos_corp_email_address: None
    osos_corp_email_address_text: None
    osos_charities_signature_block_email: None
    osos_charities_signature_block_email_no_url: None
    bi_is_other_naics: bool
    business_has_active_filings: bool
    disable_fein: bool
    disable_ubi: bool
    effective_date_flag: bool
    filing_success: bool
    is_active_filing_exist: bool
    is_additional_documents_exist: bool
    is_agent_edit_show: bool
    is_agent_mailing_address_returned_mail: bool
    is_agent_street_address_returned_mail: bool
    is_amendment_adoption_change: bool
    is_amendment_corp_shares_change: bool
    is_amendment_delinquent_status: bool
    is_amendment_duration_change: bool
    is_amendment_effective_change: bool
    is_amendment_entity_name_change: bool
    is_amendment_entity_type: bool
    is_amendment_periodof_duration: bool
    is_applicant_address_returned_mail: bool
    is_batch_job_schedule: bool
    is_business_hide: bool
    is_business_name_available: bool
    is_certificateof_existence: bool
    is_certificate_of_existence_present: bool
    is_charitable: bool
    is_client_address_returned_mail: bool
    is_consildation_in_corp: bool
    is_correspondence_address: bool
    is_dba_in_use: bool
    is_dba_name_available: bool
    is_dba_section_exist: bool
    is_domestic_ubi: bool
    is_eligible_filing_type: bool
    is_email_option_checked: bool
    is_email_option_hide: bool
    is_formation: bool
    is_formation_with_intial_report: bool
    is_grange_address_returned_mail: bool
    is_inhouse_review_or_filing: bool
    is_initial_report_filed: bool
    is_meeting_address_returned_mail: bool
    is_name_reserved: bool
    is_online: bool
    is_perpetual: bool
    is_po_mailing_address_returned_mail: bool
    is_po_street_address_returned_mail: bool
    is_ra_lookup_enabled: bool
    is_reveiw_pdf_fields_show: bool
    is_save_close_with_initial_report: bool
    is_tm_applicant_address_returned_mail: bool
    is_tm_owner_address_returned_mail: bool
    is_trade_mark_hide: bool
    is_trademark_applicant_address: bool
    is_trademark_owner_address: bool
    is_transaction_fulfilled: bool
    is_unanswered_or_blank: bool
    is_upload_document_exist: bool
    is_walk_in_close: bool
    is_walk_in_save: bool
    online_is_ubi_checked: bool
    validate_ubi_number: bool
    is_dor_question_property: bool
    is_dor_question_interest16: bool
    is_dor_question_interest50: bool
    is_dor_question_future_purchase: bool
    is_new_dor_questions_answered: bool
    action_name: None
    agent_id: int
    agent_name: str
    alternative_email: None
    amended_business_type: int
    amended_business_type_desc: None
    any_other_provisions: None
    attention: None
    available_status: None
    binaics_code: None
    binaics_code_desc: None
    bi_other_description: None
    business_category_id: int
    business_category: None
    business_id: int
    business_i_ds: None
    business_indicator: None
    business_name: str
    business_status: str
    business_status_id: int
    business_name_search: None
    business_partnership_engages: None
    business_type: str
    business_type_id: int
    cart_status: None
    confirmation_letter_document_id: int
    confirmation_letter_file_name: None
    congratulation_letter_file_name: None
    controller_name: None
    correspondence_email_address: None
    correspondence_file_name: None
    created_by: int
    created_ip: None
    date_began_doing_business_in_wa_type: None
    date_of_adoption_type: None
    dba_business_name: None
    document_id: int
    document_type_id: int
    duration_type: None
    duration_years: int
    effective_date_type: None
    file_location_online_initial_report: None
    file_location_confirmation_letter: None
    fein_no: str
    filing_correspondence_address_file_location: None
    filing_correspondence_address_file_name: None
    file_location_congratulation_letter: None
    file_location_correspondence: None
    file_location_online_report: None
    file_location_receipt: None
    initial_report_review_html: None
    is_annual_report_filed_count: int
    is_fee_waiver_full_filled_count: int
    jurisdiction: int
    jurisdiction_category: None
    jurisdiction_category_review: None
    jurisdiction_country: int
    jurisdiction_country_desc: None
    jurisdiction_country_desc_review: None
    jurisdiction_country_review: int
    jurisdiction_desc: None
    jurisdiction_desc_review: None
    jurisdiction_review: int
    jurisdiction_state: int
    jurisdiction_state_desc: None
    jurisdiction_state_desc_review: None
    jurisdiction_state_review: int
    new_business_name: None
    new_dba_business_name: None
    name_in_home_jurisdiction: None
    name_reserved_id: int
    navigate_url: None
    new_business_status_id: int
    new_filing_history: None
    new_name_in_home_jurisdiction: None
    notification_attention: None
    old_business_name: None
    old_dba_business_name: None
    old_filing_history: None
    old_jurisdiction_desc: None
    online_cart_draft_id: int
    online_initial_report_file_name: None
    online_initial_report_document_id: int
    online_lookup_ubi_no: None
    online_navigation_url: None
    online_report_document_id: int
    online_report_file_name: None
    other_provisions: None
    placeof_formation_id: None
    purpose_and_powers_id: int
    review_html: None
    receipt_file_name: None
    reprort_agent_full_address: None
    reprort_correspondence_full_address: None
    reprort_full_address: None
    save_close_exception_count: int
    save_close_notes_count: int
    seq_number: int
    temp_table_id: int
    trademark_enity_name: None
    trademark_owner_entity_name: None
    trademark_owner_address_file_name: None
    trademark_owner_address_file_name_location: None
    trademark_owner_full_name: None
    trademark_owner_full_address: None
    trademark_owner_first_name: None
    trademark_owner_last_name: None
    ubi_business_type: None
    ubi_business_type_id: int
    ubi_number: str
    has_member_non_profit: None
    has_incorporator: None
    has_board_of_directors: None
    is_can_be_public_benefit_non_profit: None
    is_elect_to_be_public_benefit_non_profit: None
    is_rcw_election: None
    is_non_profit_exempt: None
    is_can_be_host_home: None
    non_profit_reporting1: None
    non_profit_reporting2: None
    is_amendment_deliquent_status: bool
    is_incorporator_signature_attestation: None
    existing_is_rcw_election: None
    existing_is_incorporator_signature_attestation: None
    existing_is_charitable_non_profit: bool
    existing_is_host_home: bool
    existing_is_gross_revenue_non_profit: bool
    existing_is_public_benefit_non_profit: bool
    existing_has_member_non_profit: bool
    existing_fein_no: str
    is_hide_business_information_np_checkboxes: bool

    def __init__(self, is_available: bool, principal_office: BusinessInfoPrincipalOffice, principal_office_in_wa: None, agent: None, principals_list: None, principal_name: None, search_criteria: None, search_type: None, search_type_text: None, search_value: None, search_entity_name: None, start_date_of_incorporation: datetime, end_date_of_incorporation: datetime, expiration_date: datetime, criteria: Optional[Criteria], grange_address: None, meeting_place: None, is_org_business_name: bool, check_business_name: None, plus_or_minus_order: int, filtere_record_id: int, modified_date: datetime, dissolution_days: int, id: int, is_inhouse: bool, fee_list: None, ubi_status: None, is_ubi_number: bool, new_ubi_number: None, is_show_advance_search: bool, entity_name: None, status: None, type: None, is_host_home_search: None, is_public_benefit_non_profit_search: None, is_charitable_non_profit_search: None, is_gross_revenue_non_profit_search: None, is_has_members_search: None, is_has_fein_search: None, fein_no_search: None, is_host_home: None, is_public_benefit_non_profit: None, is_charitable_non_profit: None, is_gross_revenue_non_profit: None, is_has_members: None, is_has_fein: None, is_host_home_confirm: bool, entity_types_with_screens: AllScreenParts, all_screen_parts: AllScreenParts, online_report_principal_list: None, online_upload_documents_list: List[Any], upload_documents_list: List[Any], principal_member_list: List[Any], correspondence_address: Address, online_report_agent: Agent, trademark_owner_agent: Agent, online_report_authorized_person: Dict[str, Optional[bool]], online_report_business_transaction: None, ar_due_date: datetime, created_date: datetime, date_began_doing_business_in_wa: datetime, date_of_adoption: datetime, date_of_formation_in_home_jurisdiction: datetime, date_of_incorporation: datetime, dissolved_date: datetime, effective_date: datetime, expiration_date_review: datetime, filing_date: datetime, next_ar_due_date: datetime, periodof_duration_date: datetime, ra_expired_date: datetime, reinstatement_dissolution_end_date: datetime, renewal_date: datetime, requalification_termination_end_date: datetime, duration_expire_date: None, in_active_date: None, last_ar_filed_date: None, name_reservation_expire_date: None, periodof_duration_date_review: None, online_report_nature_of_business: None, online_cart_entity: None, business_info_principal_office: BusinessInfoPrincipalOffice, business_info_principal_office_in_wa: BusinessInfoPrincipalOffice, online_report_principal_office: BusinessInfoPrincipalOffice, upload_documents: UploadDocuments, osos_corp_signature_block_email: None, osos_corp_email_signature: None, osos_corp_email_signature_no_email: None, osos_corp_email_address: None, osos_corp_email_address_text: None, osos_charities_signature_block_email: None, osos_charities_signature_block_email_no_url: None, bi_is_other_naics: bool, business_has_active_filings: bool, disable_fein: bool, disable_ubi: bool, effective_date_flag: bool, filing_success: bool, is_active_filing_exist: bool, is_additional_documents_exist: bool, is_agent_edit_show: bool, is_agent_mailing_address_returned_mail: bool, is_agent_street_address_returned_mail: bool, is_amendment_adoption_change: bool, is_amendment_corp_shares_change: bool, is_amendment_delinquent_status: bool, is_amendment_duration_change: bool, is_amendment_effective_change: bool, is_amendment_entity_name_change: bool, is_amendment_entity_type: bool, is_amendment_periodof_duration: bool, is_applicant_address_returned_mail: bool, is_batch_job_schedule: bool, is_business_hide: bool, is_business_name_available: bool, is_certificateof_existence: bool, is_certificate_of_existence_present: bool, is_charitable: bool, is_client_address_returned_mail: bool, is_consildation_in_corp: bool, is_correspondence_address: bool, is_dba_in_use: bool, is_dba_name_available: bool, is_dba_section_exist: bool, is_domestic_ubi: bool, is_eligible_filing_type: bool, is_email_option_checked: bool, is_email_option_hide: bool, is_formation: bool, is_formation_with_intial_report: bool, is_grange_address_returned_mail: bool, is_inhouse_review_or_filing: bool, is_initial_report_filed: bool, is_meeting_address_returned_mail: bool, is_name_reserved: bool, is_online: bool, is_perpetual: bool, is_po_mailing_address_returned_mail: bool, is_po_street_address_returned_mail: bool, is_ra_lookup_enabled: bool, is_reveiw_pdf_fields_show: bool, is_save_close_with_initial_report: bool, is_tm_applicant_address_returned_mail: bool, is_tm_owner_address_returned_mail: bool, is_trade_mark_hide: bool, is_trademark_applicant_address: bool, is_trademark_owner_address: bool, is_transaction_fulfilled: bool, is_unanswered_or_blank: bool, is_upload_document_exist: bool, is_walk_in_close: bool, is_walk_in_save: bool, online_is_ubi_checked: bool, validate_ubi_number: bool, is_dor_question_property: bool, is_dor_question_interest16: bool, is_dor_question_interest50: bool, is_dor_question_future_purchase: bool, is_new_dor_questions_answered: bool, action_name: None, agent_id: int, agent_name: str, alternative_email: None, amended_business_type: int, amended_business_type_desc: None, any_other_provisions: None, attention: None, available_status: None, binaics_code: None, binaics_code_desc: None, bi_other_description: None, business_category_id: int, business_category: None, business_id: int, business_i_ds: None, business_indicator: None, business_name: str, business_status: str, business_status_id: int, business_name_search: None, business_partnership_engages: None, business_type: str, business_type_id: int, cart_status: None, confirmation_letter_document_id: int, confirmation_letter_file_name: None, congratulation_letter_file_name: None, controller_name: None, correspondence_email_address: None, correspondence_file_name: None, created_by: int, created_ip: None, date_began_doing_business_in_wa_type: None, date_of_adoption_type: None, dba_business_name: None, document_id: int, document_type_id: int, duration_type: None, duration_years: int, effective_date_type: None, file_location_online_initial_report: None, file_location_confirmation_letter: None, fein_no: str, filing_correspondence_address_file_location: None, filing_correspondence_address_file_name: None, file_location_congratulation_letter: None, file_location_correspondence: None, file_location_online_report: None, file_location_receipt: None, initial_report_review_html: None, is_annual_report_filed_count: int, is_fee_waiver_full_filled_count: int, jurisdiction: int, jurisdiction_category: None, jurisdiction_category_review: None, jurisdiction_country: int, jurisdiction_country_desc: None, jurisdiction_country_desc_review: None, jurisdiction_country_review: int, jurisdiction_desc: None, jurisdiction_desc_review: None, jurisdiction_review: int, jurisdiction_state: int, jurisdiction_state_desc: None, jurisdiction_state_desc_review: None, jurisdiction_state_review: int, new_business_name: None, new_dba_business_name: None, name_in_home_jurisdiction: None, name_reserved_id: int, navigate_url: None, new_business_status_id: int, new_filing_history: None, new_name_in_home_jurisdiction: None, notification_attention: None, old_business_name: None, old_dba_business_name: None, old_filing_history: None, old_jurisdiction_desc: None, online_cart_draft_id: int, online_initial_report_file_name: None, online_initial_report_document_id: int, online_lookup_ubi_no: None, online_navigation_url: None, online_report_document_id: int, online_report_file_name: None, other_provisions: None, placeof_formation_id: None, purpose_and_powers_id: int, review_html: None, receipt_file_name: None, reprort_agent_full_address: None, reprort_correspondence_full_address: None, reprort_full_address: None, save_close_exception_count: int, save_close_notes_count: int, seq_number: int, temp_table_id: int, trademark_enity_name: None, trademark_owner_entity_name: None, trademark_owner_address_file_name: None, trademark_owner_address_file_name_location: None, trademark_owner_full_name: None, trademark_owner_full_address: None, trademark_owner_first_name: None, trademark_owner_last_name: None, ubi_business_type: None, ubi_business_type_id: int, ubi_number: str, has_member_non_profit: None, has_incorporator: None, has_board_of_directors: None, is_can_be_public_benefit_non_profit: None, is_elect_to_be_public_benefit_non_profit: None, is_rcw_election: None, is_non_profit_exempt: None, is_can_be_host_home: None, non_profit_reporting1: None, non_profit_reporting2: None, is_amendment_deliquent_status: bool, is_incorporator_signature_attestation: None, existing_is_rcw_election: None, existing_is_incorporator_signature_attestation: None, existing_is_charitable_non_profit: bool, existing_is_host_home: bool, existing_is_gross_revenue_non_profit: bool, existing_is_public_benefit_non_profit: bool, existing_has_member_non_profit: bool, existing_fein_no: str, is_hide_business_information_np_checkboxes: bool) -> None:
        self.is_available = is_available
        self.principal_office = principal_office
        self.principal_office_in_wa = principal_office_in_wa
        self.agent = agent
        self.principals_list = principals_list
        self.principal_name = principal_name
        self.search_criteria = search_criteria
        self.search_type = search_type
        self.search_type_text = search_type_text
        self.search_value = search_value
        self.search_entity_name = search_entity_name
        self.start_date_of_incorporation = start_date_of_incorporation
        self.end_date_of_incorporation = end_date_of_incorporation
        self.expiration_date = expiration_date
        self.criteria = criteria
        self.grange_address = grange_address
        self.meeting_place = meeting_place
        self.is_org_business_name = is_org_business_name
        self.check_business_name = check_business_name
        self.plus_or_minus_order = plus_or_minus_order
        self.filtere_record_id = filtere_record_id
        self.modified_date = modified_date
        self.dissolution_days = dissolution_days
        self.id = id
        self.is_inhouse = is_inhouse
        self.fee_list = fee_list
        self.ubi_status = ubi_status
        self.is_ubi_number = is_ubi_number
        self.new_ubi_number = new_ubi_number
        self.is_show_advance_search = is_show_advance_search
        self.entity_name = entity_name
        self.status = status
        self.type = type
        self.is_host_home_search = is_host_home_search
        self.is_public_benefit_non_profit_search = is_public_benefit_non_profit_search
        self.is_charitable_non_profit_search = is_charitable_non_profit_search
        self.is_gross_revenue_non_profit_search = is_gross_revenue_non_profit_search
        self.is_has_members_search = is_has_members_search
        self.is_has_fein_search = is_has_fein_search
        self.fein_no_search = fein_no_search
        self.is_host_home = is_host_home
        self.is_public_benefit_non_profit = is_public_benefit_non_profit
        self.is_charitable_non_profit = is_charitable_non_profit
        self.is_gross_revenue_non_profit = is_gross_revenue_non_profit
        self.is_has_members = is_has_members
        self.is_has_fein = is_has_fein
        self.is_host_home_confirm = is_host_home_confirm
        self.entity_types_with_screens = entity_types_with_screens
        self.all_screen_parts = all_screen_parts
        self.online_report_principal_list = online_report_principal_list
        self.online_upload_documents_list = online_upload_documents_list
        self.upload_documents_list = upload_documents_list
        self.principal_member_list = principal_member_list
        self.correspondence_address = correspondence_address
        self.online_report_agent = online_report_agent
        self.trademark_owner_agent = trademark_owner_agent
        self.online_report_authorized_person = online_report_authorized_person
        self.online_report_business_transaction = online_report_business_transaction
        self.ar_due_date = ar_due_date
        self.created_date = created_date
        self.date_began_doing_business_in_wa = date_began_doing_business_in_wa
        self.date_of_adoption = date_of_adoption
        self.date_of_formation_in_home_jurisdiction = date_of_formation_in_home_jurisdiction
        self.date_of_incorporation = date_of_incorporation
        self.dissolved_date = dissolved_date
        self.effective_date = effective_date
        self.expiration_date_review = expiration_date_review
        self.filing_date = filing_date
        self.next_ar_due_date = next_ar_due_date
        self.periodof_duration_date = periodof_duration_date
        self.ra_expired_date = ra_expired_date
        self.reinstatement_dissolution_end_date = reinstatement_dissolution_end_date
        self.renewal_date = renewal_date
        self.requalification_termination_end_date = requalification_termination_end_date
        self.duration_expire_date = duration_expire_date
        self.in_active_date = in_active_date
        self.last_ar_filed_date = last_ar_filed_date
        self.name_reservation_expire_date = name_reservation_expire_date
        self.periodof_duration_date_review = periodof_duration_date_review
        self.online_report_nature_of_business = online_report_nature_of_business
        self.online_cart_entity = online_cart_entity
        self.business_info_principal_office = business_info_principal_office
        self.business_info_principal_office_in_wa = business_info_principal_office_in_wa
        self.online_report_principal_office = online_report_principal_office
        self.upload_documents = upload_documents
        self.osos_corp_signature_block_email = osos_corp_signature_block_email
        self.osos_corp_email_signature = osos_corp_email_signature
        self.osos_corp_email_signature_no_email = osos_corp_email_signature_no_email
        self.osos_corp_email_address = osos_corp_email_address
        self.osos_corp_email_address_text = osos_corp_email_address_text
        self.osos_charities_signature_block_email = osos_charities_signature_block_email
        self.osos_charities_signature_block_email_no_url = osos_charities_signature_block_email_no_url
        self.bi_is_other_naics = bi_is_other_naics
        self.business_has_active_filings = business_has_active_filings
        self.disable_fein = disable_fein
        self.disable_ubi = disable_ubi
        self.effective_date_flag = effective_date_flag
        self.filing_success = filing_success
        self.is_active_filing_exist = is_active_filing_exist
        self.is_additional_documents_exist = is_additional_documents_exist
        self.is_agent_edit_show = is_agent_edit_show
        self.is_agent_mailing_address_returned_mail = is_agent_mailing_address_returned_mail
        self.is_agent_street_address_returned_mail = is_agent_street_address_returned_mail
        self.is_amendment_adoption_change = is_amendment_adoption_change
        self.is_amendment_corp_shares_change = is_amendment_corp_shares_change
        self.is_amendment_delinquent_status = is_amendment_delinquent_status
        self.is_amendment_duration_change = is_amendment_duration_change
        self.is_amendment_effective_change = is_amendment_effective_change
        self.is_amendment_entity_name_change = is_amendment_entity_name_change
        self.is_amendment_entity_type = is_amendment_entity_type
        self.is_amendment_periodof_duration = is_amendment_periodof_duration
        self.is_applicant_address_returned_mail = is_applicant_address_returned_mail
        self.is_batch_job_schedule = is_batch_job_schedule
        self.is_business_hide = is_business_hide
        self.is_business_name_available = is_business_name_available
        self.is_certificateof_existence = is_certificateof_existence
        self.is_certificate_of_existence_present = is_certificate_of_existence_present
        self.is_charitable = is_charitable
        self.is_client_address_returned_mail = is_client_address_returned_mail
        self.is_consildation_in_corp = is_consildation_in_corp
        self.is_correspondence_address = is_correspondence_address
        self.is_dba_in_use = is_dba_in_use
        self.is_dba_name_available = is_dba_name_available
        self.is_dba_section_exist = is_dba_section_exist
        self.is_domestic_ubi = is_domestic_ubi
        self.is_eligible_filing_type = is_eligible_filing_type
        self.is_email_option_checked = is_email_option_checked
        self.is_email_option_hide = is_email_option_hide
        self.is_formation = is_formation
        self.is_formation_with_intial_report = is_formation_with_intial_report
        self.is_grange_address_returned_mail = is_grange_address_returned_mail
        self.is_inhouse_review_or_filing = is_inhouse_review_or_filing
        self.is_initial_report_filed = is_initial_report_filed
        self.is_meeting_address_returned_mail = is_meeting_address_returned_mail
        self.is_name_reserved = is_name_reserved
        self.is_online = is_online
        self.is_perpetual = is_perpetual
        self.is_po_mailing_address_returned_mail = is_po_mailing_address_returned_mail
        self.is_po_street_address_returned_mail = is_po_street_address_returned_mail
        self.is_ra_lookup_enabled = is_ra_lookup_enabled
        self.is_reveiw_pdf_fields_show = is_reveiw_pdf_fields_show
        self.is_save_close_with_initial_report = is_save_close_with_initial_report
        self.is_tm_applicant_address_returned_mail = is_tm_applicant_address_returned_mail
        self.is_tm_owner_address_returned_mail = is_tm_owner_address_returned_mail
        self.is_trade_mark_hide = is_trade_mark_hide
        self.is_trademark_applicant_address = is_trademark_applicant_address
        self.is_trademark_owner_address = is_trademark_owner_address
        self.is_transaction_fulfilled = is_transaction_fulfilled
        self.is_unanswered_or_blank = is_unanswered_or_blank
        self.is_upload_document_exist = is_upload_document_exist
        self.is_walk_in_close = is_walk_in_close
        self.is_walk_in_save = is_walk_in_save
        self.online_is_ubi_checked = online_is_ubi_checked
        self.validate_ubi_number = validate_ubi_number
        self.is_dor_question_property = is_dor_question_property
        self.is_dor_question_interest16 = is_dor_question_interest16
        self.is_dor_question_interest50 = is_dor_question_interest50
        self.is_dor_question_future_purchase = is_dor_question_future_purchase
        self.is_new_dor_questions_answered = is_new_dor_questions_answered
        self.action_name = action_name
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.alternative_email = alternative_email
        self.amended_business_type = amended_business_type
        self.amended_business_type_desc = amended_business_type_desc
        self.any_other_provisions = any_other_provisions
        self.attention = attention
        self.available_status = available_status
        self.binaics_code = binaics_code
        self.binaics_code_desc = binaics_code_desc
        self.bi_other_description = bi_other_description
        self.business_category_id = business_category_id
        self.business_category = business_category
        self.business_id = business_id
        self.business_i_ds = business_i_ds
        self.business_indicator = business_indicator
        self.business_name = business_name
        self.business_status = business_status
        self.business_status_id = business_status_id
        self.business_name_search = business_name_search
        self.business_partnership_engages = business_partnership_engages
        self.business_type = business_type
        self.business_type_id = business_type_id
        self.cart_status = cart_status
        self.confirmation_letter_document_id = confirmation_letter_document_id
        self.confirmation_letter_file_name = confirmation_letter_file_name
        self.congratulation_letter_file_name = congratulation_letter_file_name
        self.controller_name = controller_name
        self.correspondence_email_address = correspondence_email_address
        self.correspondence_file_name = correspondence_file_name
        self.created_by = created_by
        self.created_ip = created_ip
        self.date_began_doing_business_in_wa_type = date_began_doing_business_in_wa_type
        self.date_of_adoption_type = date_of_adoption_type
        self.dba_business_name = dba_business_name
        self.document_id = document_id
        self.document_type_id = document_type_id
        self.duration_type = duration_type
        self.duration_years = duration_years
        self.effective_date_type = effective_date_type
        self.file_location_online_initial_report = file_location_online_initial_report
        self.file_location_confirmation_letter = file_location_confirmation_letter
        self.fein_no = fein_no
        self.filing_correspondence_address_file_location = filing_correspondence_address_file_location
        self.filing_correspondence_address_file_name = filing_correspondence_address_file_name
        self.file_location_congratulation_letter = file_location_congratulation_letter
        self.file_location_correspondence = file_location_correspondence
        self.file_location_online_report = file_location_online_report
        self.file_location_receipt = file_location_receipt
        self.initial_report_review_html = initial_report_review_html
        self.is_annual_report_filed_count = is_annual_report_filed_count
        self.is_fee_waiver_full_filled_count = is_fee_waiver_full_filled_count
        self.jurisdiction = jurisdiction
        self.jurisdiction_category = jurisdiction_category
        self.jurisdiction_category_review = jurisdiction_category_review
        self.jurisdiction_country = jurisdiction_country
        self.jurisdiction_country_desc = jurisdiction_country_desc
        self.jurisdiction_country_desc_review = jurisdiction_country_desc_review
        self.jurisdiction_country_review = jurisdiction_country_review
        self.jurisdiction_desc = jurisdiction_desc
        self.jurisdiction_desc_review = jurisdiction_desc_review
        self.jurisdiction_review = jurisdiction_review
        self.jurisdiction_state = jurisdiction_state
        self.jurisdiction_state_desc = jurisdiction_state_desc
        self.jurisdiction_state_desc_review = jurisdiction_state_desc_review
        self.jurisdiction_state_review = jurisdiction_state_review
        self.new_business_name = new_business_name
        self.new_dba_business_name = new_dba_business_name
        self.name_in_home_jurisdiction = name_in_home_jurisdiction
        self.name_reserved_id = name_reserved_id
        self.navigate_url = navigate_url
        self.new_business_status_id = new_business_status_id
        self.new_filing_history = new_filing_history
        self.new_name_in_home_jurisdiction = new_name_in_home_jurisdiction
        self.notification_attention = notification_attention
        self.old_business_name = old_business_name
        self.old_dba_business_name = old_dba_business_name
        self.old_filing_history = old_filing_history
        self.old_jurisdiction_desc = old_jurisdiction_desc
        self.online_cart_draft_id = online_cart_draft_id
        self.online_initial_report_file_name = online_initial_report_file_name
        self.online_initial_report_document_id = online_initial_report_document_id
        self.online_lookup_ubi_no = online_lookup_ubi_no
        self.online_navigation_url = online_navigation_url
        self.online_report_document_id = online_report_document_id
        self.online_report_file_name = online_report_file_name
        self.other_provisions = other_provisions
        self.placeof_formation_id = placeof_formation_id
        self.purpose_and_powers_id = purpose_and_powers_id
        self.review_html = review_html
        self.receipt_file_name = receipt_file_name
        self.reprort_agent_full_address = reprort_agent_full_address
        self.reprort_correspondence_full_address = reprort_correspondence_full_address
        self.reprort_full_address = reprort_full_address
        self.save_close_exception_count = save_close_exception_count
        self.save_close_notes_count = save_close_notes_count
        self.seq_number = seq_number
        self.temp_table_id = temp_table_id
        self.trademark_enity_name = trademark_enity_name
        self.trademark_owner_entity_name = trademark_owner_entity_name
        self.trademark_owner_address_file_name = trademark_owner_address_file_name
        self.trademark_owner_address_file_name_location = trademark_owner_address_file_name_location
        self.trademark_owner_full_name = trademark_owner_full_name
        self.trademark_owner_full_address = trademark_owner_full_address
        self.trademark_owner_first_name = trademark_owner_first_name
        self.trademark_owner_last_name = trademark_owner_last_name
        self.ubi_business_type = ubi_business_type
        self.ubi_business_type_id = ubi_business_type_id
        self.ubi_number = ubi_number
        self.has_member_non_profit = has_member_non_profit
        self.has_incorporator = has_incorporator
        self.has_board_of_directors = has_board_of_directors
        self.is_can_be_public_benefit_non_profit = is_can_be_public_benefit_non_profit
        self.is_elect_to_be_public_benefit_non_profit = is_elect_to_be_public_benefit_non_profit
        self.is_rcw_election = is_rcw_election
        self.is_non_profit_exempt = is_non_profit_exempt
        self.is_can_be_host_home = is_can_be_host_home
        self.non_profit_reporting1 = non_profit_reporting1
        self.non_profit_reporting2 = non_profit_reporting2
        self.is_amendment_deliquent_status = is_amendment_deliquent_status
        self.is_incorporator_signature_attestation = is_incorporator_signature_attestation
        self.existing_is_rcw_election = existing_is_rcw_election
        self.existing_is_incorporator_signature_attestation = existing_is_incorporator_signature_attestation
        self.existing_is_charitable_non_profit = existing_is_charitable_non_profit
        self.existing_is_host_home = existing_is_host_home
        self.existing_is_gross_revenue_non_profit = existing_is_gross_revenue_non_profit
        self.existing_is_public_benefit_non_profit = existing_is_public_benefit_non_profit
        self.existing_has_member_non_profit = existing_has_member_non_profit
        self.existing_fein_no = existing_fein_no
        self.is_hide_business_information_np_checkboxes = is_hide_business_information_np_checkboxes
