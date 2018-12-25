""" Constants for pytw module """

""" Constants for REST API calls """
HTTPS_PREFIX = "https://"
API_BASE_URL = "api/"
API_VERSION_1 = "v1/"
API_VERSION_2 = "v2/"
VULNS_URL = "vulns/"
IMPACTS_URL = "impacts/"
ASSETS_URL = "assets/"
URL_FORWARD_SLASH = "/"

""" Some common fields """
ID = "id"
RATING = "rating"

""" Fields of Vuln Object """
VULN_ID = "id"
VULN_TITLE = "title"
VULN_SUMMARY = "summary"
VULN_VULNERABILITY_TYPES = "vulnerability_types"
VULN_CVSS_VECTOR = "cvss_vector"
VULN_CVSS_SCORE = "cvss_score"
VULN_PUBLISHER = "publisher"
VULN_PUBLISHED_DATETIME = "published"
VULN_LAST_MODIFIED_DATETIME = "last_modified"
VULN_NOTIONAL_LAST_MODIFIED_DATETIME = "notional_last_modified"
VULN_LAST_CHANGE = "last_change"
VULN_PRODUCTS = "products"
VULN_PRODUCT_NAME = "name"
VULN_PRODUCT_VENDOR = "vendor"
VULN_PRODUCT_VERSION = "version"
VULN_EXPLOITS = "exploits"
VULN_EXPLOIT_SOURCE = "source"
VULN_EXPLOIT_URL = "url"
VULN_REMEDIATIONS = "remediations"
VULN_REMEDIATION_SOURCE = "source"
VULN_REMEDIATION_URL = "url"
VULN_REMEDIATION_DESCRIPTION = "description"
VULN_REFERENCES = "references"
VULN_ADVISORIES = "advisories"
VULN_RELATED_VULNS = "related_vulns"
VULN_PATCHES = "patches"
VULN_PATCH_ID = "id"
VULN_PATCH_PRODUCT = "product"
VULN_PATCH_URL = "url"
VULN_PATCH_DESCRIPTION = "description"

""" Fields of VulnImpact object """
IMPACT_VULN_ID = "vuln_id"
IMPACT_ASSET_ID = "asset_id"
IMPACT_PRODUCT = "product"
IMPACT_KEYWORD = "keyword"
IMPACT_CONFIDENCE = "confidence"
IMPACT_STATUS = "status"
IMPACT_TIMESTAMP = "timestamp"
IMPACT_VULNERABILITY = "vulnerability"

""" Fields of Asset object """
ASSET_ID = "id"
ASSET_NAME = "name"
ASSET_TYPE = "type"
ASSET_DESCRIPTION = "description"
ASSET_LOCATION = "location"
ASSET_PRODUCTS = "products"
ASSET_PATCHES = "patches"
ASSET_OWNER = "owner"
ASSET_NOTIFY = "notify"
ASSET_TAGS = "tags"


""" Search Parameters related constants """
SEARCH_PARAM_WINDOW_START = "window_start"
SEARCH_PARAM_WINDOW_END = "window_end"
SEARCH_PARAM_OFFSET = "offset"
SEARCH_PARAM_LIMIT = "limit"
SEARCH_PARAM_RATINGS = "ratings"
SEARCH_PARAM_PUBLISHERS = "publishers"
SEARCH_PARAM_FREE_TEXT_SEARCH = "search"
SEARCH_PARAM_THRESHOLD = "threshold"
SEARCH_PARAM_IMPACT_STATUS = "status"
SEARCH_PARAM_ASSET_IDS = "asset_ids"
SEARCH_PARAM_VULN_IDS = "vuln_ids"
SEARCH_PARAM_FILTERS = "filters"
SEARCH_PARAM_ASSET_ID = "asset_id"
SEARCH_PARAM_ASSET_TYPES = "types"
SEARCH_PARAM_ASSET_NAMES = "names"
SEARCH_PARAM_ASSET_LOCATIONS = "locations"
SEARCH_PARAM_ASSET_PRODUCT = "product"
SEARCH_PARAM_ASSET_PATCH = "patch"

""" Predefined Search Filters """
SEARCH_FILTER_RECENT = "recent"
SEARCH_FILTER_THREATFILTER = "threatfilter"
SEARCH_FILTER_EXPLOITABLE = "exploitable"
SEARCH_FILTER_PATCH_AVAILABLE = "patch-available"
SEARCH_FILTER_REMEDIATION_AVAILABLE = "remediation-available"
SEARCH_FILTER_TRACKED_VULNS = "tracked"
SEARCH_FILTER_ASSETS_WITH_OPEN_IMPACTS = "assets_with_open_impacts"
SEARCH_FILTER_MY_ASSETS = "my_assets"

