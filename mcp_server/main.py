# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:52:01+00:00



import argparse
import json
import os
from typing import *
from typing import Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity, UnsuportedSecurityStub
from fastapi import Path, Query

from models import (
    AcceptPaymentDisputeRequest,
    AddEvidencePaymentDisputeRequest,
    AddEvidencePaymentDisputeResponse,
    ContestPaymentDisputeRequest,
    DisputeSummaryResponse,
    FileEvidence,
    IssueRefundRequest,
    Order,
    OrderOrderIdShippingFulfillmentPostResponse,
    OrderSearchPagedCollection,
    PaymentDispute,
    PaymentDisputeActivityHistory,
    PaymentDisputePaymentDisputeIdFetchEvidenceContentGetResponse,
    Refund,
    ShippingFulfillment,
    ShippingFulfillmentDetails,
    ShippingFulfillmentPagedCollection,
    UpdateEvidencePaymentDisputeRequest,
)

app = MCPProxy(
    contact={'name': 'eBay Inc.', 'x-twitter': 'ebay'},
    description='Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.',
    license={
        'name': 'eBay API License Agreement',
        'url': 'https://go.developer.ebay.com/api-license-agreement',
    },
    title='Fulfillment API',
    version='v1.19.19',
    servers=[
        {
            'description': 'Production',
            'url': 'https://api.ebay.com{basePath}',
            'variables': {'basePath': {'default': '/sell/fulfillment/v1'}},
        },
        {
            'description': 'Production',
            'url': 'https://apiz.ebay.com{basePath}',
            'variables': {'basePath': {'default': '/sell/fulfillment/v1'}},
        },
    ],
)


@app.get(
    '/order',
    description=""" Use this call to search for and retrieve one or more orders based on their creation date, last modification date, or fulfillment status using the <b>filter</b> parameter. You can alternatively specify a list of orders using the <b>orderIds</b> parameter. Include the optional <b>fieldGroups</b> query parameter set to <code>TAX_BREAKDOWN</code> to return a breakdown of the taxes and fees. <br><br> The returned <b>Order</b> objects contain information you can use to create and process fulfillments, including: <ul> <li>Information about the buyer and seller</li> <li>Information about the order's line items</li> <li>The plans for packaging, addressing and shipping the order</li> <li>The status of payment, packaging, addressing, and shipping the order</li> <li>A summary of monetary amounts specific to the order such as pricing, payments, and shipping costs</li> <li>A summary of applied taxes and fees, and optionally a breakdown of each </li></ul> <br><br> <span class="tablenote"><strong>Important:</strong> In this call, the <b>cancelStatus.cancelRequests</b> array is returned but is always empty. Use the <b>getOrder</b> call instead, which returns this array fully populated with information about any cancellation requests.</span> """,
    tags=['order_processing', 'fulfillment_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_orders(
    field_groups: Optional[str] = Query(None, alias='fieldGroups'),
    filter: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
    order_ids: Optional[str] = Query(None, alias='orderIds'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/order/{orderId}',
    description=""" Use this call to retrieve the contents of an order based on its unique identifier, <i>orderId</i>. This value was returned in the <b> getOrders</b> call's <b>orders.orderId</b> field when you searched for orders by creation date, modification date, or fulfillment status. Include the optional <b>fieldGroups</b> query parameter set to <code>TAX_BREAKDOWN</code> to return a breakdown of the taxes and fees. <br><br> The returned <b>Order</b> object contains information you can use to create and process fulfillments, including: <ul> <li>Information about the buyer and seller</li> <li>Information about the order's line items</li> <li> The plans for packaging, addressing and shipping the order</li> <li>The status of payment, packaging, addressing, and shipping the order</li> <li>A summary of monetary amounts specific to the order such as pricing, payments, and shipping costs</li> <li>A summary of applied taxes and fees, and optionally a breakdown of each </li></ul> """,
    tags=['order_processing', 'fulfillment_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_order(
    field_groups: Optional[str] = Query(None, alias='fieldGroups'),
    order_id: str = Path(..., alias='orderId'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/order/{orderId}/shipping_fulfillment',
    description=""" Use this call to retrieve the contents of all fulfillments currently defined for a specified order based on the order's unique identifier, <b>orderId</b>. This value is returned in the <b>getOrders</b> call's <b>members.orderId</b> field when you search for orders by creation date or shipment status. """,
    tags=['order_processing'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_shipping_fulfillments(order_id: str = Path(..., alias='orderId')):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/order/{orderId}/shipping_fulfillment',
    description=""" When you group an order's line items into one or more packages, each package requires a corresponding plan for handling, addressing, and shipping; this is a <i>shipping fulfillment</i>. For each package, execute this call once to generate a shipping fulfillment associated with that package. <br><br> <span class="tablenote"><strong>Note:</strong> A single line item in an order can consist of multiple units of a purchased item, and one unit can consist of multiple parts or components. Although these components might be provided by the manufacturer in separate packaging, the seller must include all components of a given line item in the same package.</span> <br><br>Before using this call for a given package, you must determine which line items are in the package. If the package has been shipped, you should provide the date of shipment in the request. If not provided, it will default to the current date and time. """,
    tags=['order_processing', 'fulfillment_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def create_shipping_fulfillment(
    order_id: str = Path(..., alias='orderId'), body: ShippingFulfillmentDetails = ...
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/order/{orderId}/shipping_fulfillment/{fulfillmentId}',
    description=""" Use this call to retrieve the contents of a fulfillment based on its unique identifier, <b>fulfillmentId</b> (combined with the associated order's <b>orderId</b>). The <b>fulfillmentId</b> value was originally generated by the <b>createShippingFulfillment</b> call, and is returned by the <b>getShippingFulfillments</b> call in the <b>members.fulfillmentId</b> field. """,
    tags=['order_processing', 'fulfillment_management'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_shipping_fulfillment(
    fulfillment_id: str = Path(..., alias='fulfillmentId'),
    order_id: str = Path(..., alias='orderId'),
):
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/order/{order_id}/issue_refund',
    description=""" <div class="msgbox_important"><p class="msgbox_importantInDiv" data-mc-autonum="&lt;b&gt;&lt;span style=&quot;color: #dd1e31;&quot; class=&quot;mcFormatColor&quot;&gt;Important! &lt;/span&gt;&lt;/b&gt;"><span class="autonumber"><span><b><span style="color: #dd1e31;" class="mcFormatColor">Important!</span></b></span></span> Due to EU &amp; UK Payments regulatory requirements, an additional security verification via Digital Signatures is required for certain API calls that are made on behalf of EU/UK sellers, including <b>issueRefund</b>. Please refer to <a href="/develop/guides/digital-signatures-for-apis " target="_blank">Digital Signatures for APIs</a> to learn more on the impacted APIs and the process to create signatures to be included in the HTTP payload.</p></div><br> This method allows a seller to issue a full or partial refund to a buyer for an order. Full or partial refunds can be issued at the order level or line item level.<br><br>The refunds issued through this method are processed asynchronously, so the refund will not show as 'Refunded' right away. A seller will have to make a subsequent <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder" target="_blank">getOrder</a> call to check the status of the refund.  The status of an order refund can be found in the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder#response.paymentSummary.refunds.refundStatus" target="_blank">paymentSummary.refunds.refundStatus</a> field of the <a href="/api-docs/sell/fulfillment/resources/order/methods/getOrder" target="_blank">getOrder</a> response. """,
    tags=['order_processing', 'dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def issue_refund(order_id: str, body: IssueRefundRequest = None):
    """
    Issue Refund
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/payment_dispute/{payment_dispute_id}',
    description=""" This method retrieves detailed information on a specific payment dispute. The payment dispute identifier is passed in as path parameter at the end of the call URI.<br><br>Below is a summary of the information that is retrieved:<ul><li>Current status of payment dispute</li><li>Amount of the payment dispute</li><li>Reason the payment dispute was opened</li><li>Order and line items associated with the payment dispute</li><li>Seller response options if an action is currently required on the payment dispute</li><li>Details on the results of the payment dispute if it has been closed</li><li>Details on any evidence that was provided by the seller to fight the payment dispute</li></ul> """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_payment_dispute(payment_dispute_id: str):
    """
    Get Payment Dispute Details
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/payment_dispute/{payment_dispute_id}/accept',
    description=""" This method is used if the seller wishes to accept a payment dispute. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the <strong>getPaymentDisputeSummaries</strong> method.<br><br>The <strong>revision</strong> field in the request payload is required, and the <strong>returnAddress</strong> field should be supplied if the seller is expecting the buyer to return the item. See the Request Payload section for more information on theste fields. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def accept_payment_dispute(
    payment_dispute_id: str, body: AcceptPaymentDisputeRequest = None
):
    """
    Accept Payment Dispute
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/payment_dispute/{payment_dispute_id}/activity',
    description=""" This method retrieve a log of activity for a payment dispute. The identifier of the payment dispute is passed in as a path parameter. The output includes a timestamp for each action of the payment dispute, from creation to resolution, and all steps in between. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_activities(payment_dispute_id: str):
    """
    Get Payment Dispute Activity
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/payment_dispute/{payment_dispute_id}/add_evidence',
    description=""" This method is used by the seller to add one or more evidence files to address a payment dispute initiated by the buyer. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the <strong>getPaymentDisputeSummaries</strong> method.<br><br><span class="tablenote"><strong>Note:</strong> All evidence files should be uploaded using <strong>addEvidence</strong> and <strong>updateEvidence</strong>  before the seller decides to contest the payment dispute. Once the seller has officially contested the dispute (using <strong>contestPaymentDispute</strong> or through My eBay), the <strong>addEvidence</strong> and <strong>updateEvidence</strong> methods can no longer be used. In the <strong>evidenceRequests</strong> array of the <strong>getPaymentDispute</strong> response, eBay prompts the seller with the type of evidence file(s) that will be needed to contest the payment dispute.</span><br><br>The file(s) to add are identified through the <strong>files</strong> array in the request payload.  Adding one or more new evidence files for a payment dispute triggers the creation of an evidence file, and the unique identifier for the new evidence file is automatically generated and returned in the <strong>evidenceId</strong> field of the <strong>addEvidence</strong> response payload upon a successful call.<br><br>The type of evidence being added should be specified in the <strong>evidenceType</strong> field. All files being added (if more than one) should correspond to this evidence type.<br><br>Upon a successful call, an <strong>evidenceId</strong> value is returned in the response. This indicates that a new evidence set has been created for the payment dispute, and this evidence set includes the evidence file(s) that were passed in to the <strong>fileId</strong> array. The <strong>evidenceId</strong> value will be needed if the seller wishes to add to the evidence set by using the <strong>updateEvidence</strong> method, or if they want to retrieve a specific evidence file within the evidence set by using the <strong>fetchEvidenceContent</strong> method. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def add_evidence(
    payment_dispute_id: str, body: AddEvidencePaymentDisputeRequest = None
):
    """
    Add an Evidence File
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/payment_dispute/{payment_dispute_id}/contest',
    description=""" This method is used if the seller wishes to contest a payment dispute initiated by the buyer. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the <strong>getPaymentDisputeSummaries</strong> method.<br><br><span class="tablenote"><strong>Note:</strong> Before contesting a payment dispute, the seller must upload all supporting files using the <strong>addEvidence</strong> and <strong>updateEvidence</strong> methods. Once the seller has officially contested the dispute (using <strong>contestPaymentDispute</strong>), the <strong>addEvidence</strong> and <strong>updateEvidence</strong> methods can no longer be used. In the <strong>evidenceRequests</strong> array of the <strong>getPaymentDispute</strong> response, eBay prompts the seller with the type of supporting file(s) that will be needed to contest the payment dispute.</span><br><br>If a seller decides to contest a payment dispute, that seller should be prepared to provide supporting documents such as proof of delivery, proof of authentication, or other documents. The type of supporting documents that the seller will provide will depend on why the buyer filed the payment dispute.<br><br>The <strong>revision</strong> field in the request payload is required, and the <strong>returnAddress</strong> field should be supplied if the seller is expecting the buyer to return the item. See the Request Payload section for more information on these fields. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def contest_payment_dispute(
    payment_dispute_id: str, body: ContestPaymentDisputeRequest = None
):
    """
    Contest Payment Dispute
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/payment_dispute/{payment_dispute_id}/fetch_evidence_content',
    description=""" This call retrieves a specific evidence file for a payment dispute. The following three identifying parameters are needed in the call URI:<ul><li><strong>payment_dispute_id</strong>: the identifier of the payment dispute. The identifier of each payment dispute is returned in the <strong>getPaymentDisputeSummaries</strong> response.</li><li><strong>evidence_id</strong>: the identifier of the evidential file set. The identifier of an evidential file set for a payment dispute is returned under the <strong>evidence</strong> array in the <strong>getPaymentDispute</strong> response.</li><li><strong>file_id</strong>: the identifier of an evidential file. This file must belong to the evidential file set identified through the <strong>evidence_id</strong> query parameter. The identifier of each evidential file is returned under the <strong>evidence.files</strong> array in the <strong>getPaymentDispute</strong> response.</li></ul><p>An actual binary file is returned if the call is successful. An error will occur if any of three identifiers are invalid.</p> """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def fetch_evidence_content(
    payment_dispute_id: str, evidence_id: str = ..., file_id: str = ...
):
    """
    Get Payment Dispute Evidence File
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/payment_dispute/{payment_dispute_id}/update_evidence',
    description=""" This method is used by the seller to update an existing evidence set for a payment dispute with one or more evidence files. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the <strong>getPaymentDisputeSummaries</strong> method.<br><br><span class="tablenote"><strong>Note:</strong> All evidence files should be uploaded using <strong>addEvidence</strong> and <strong>updateEvidence</strong>  before the seller decides to contest the payment dispute. Once the seller has officially contested the dispute (using <strong>contestPaymentDispute</strong> or through My eBay), the <strong>addEvidence</strong> and <strong>updateEvidence</strong> methods can no longer be used. In the <strong>evidenceRequests</strong> array of the <strong>getPaymentDispute</strong> response, eBay prompts the seller with the type of evidence file(s) that will be needed to contest the payment dispute.</span><br><br>The unique identifier of the evidence set to update is specified through the <strong>evidenceId</strong> field, and the file(s) to add are identified through the <strong>files</strong> array in the request payload. The unique identifier for an evidence file is automatically generated and returned in the <strong>fileId</strong> field of the <strong>uploadEvidence</strong> response payload upon a successful call. Sellers must make sure to capture the <strong>fileId</strong> value for each evidence file that is uploaded with the <strong>uploadEvidence</strong> method.<br><br>The type of evidence being added should be specified in the <strong>evidenceType</strong> field.  All files being added (if more than one) should correspond to this evidence type.<br><br>Upon a successful call, an http status code of <code>204 Success</code> is returned. There is no response payload unless an error occurs. To verify that a new file is a part of the evidence set, the seller can use the <strong>fetchEvidenceContent</strong> method, passing in the proper <strong>evidenceId</strong> and <strong>fileId</strong> values. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def update_evidence(
    payment_dispute_id: str, body: UpdateEvidencePaymentDisputeRequest = None
):
    """
    Update evidence
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/payment_dispute/{payment_dispute_id}/upload_evidence_file',
    description=""" This method is used to upload an evidence file for a contested payment dispute. The unique identifier of the payment dispute is passed in as a path parameter, and unique identifiers for payment disputes can be retrieved with the <strong>getPaymentDisputeSummaries</strong> method.<br><br><span class="tablenote"><strong>Note:</strong> The <strong>uploadEvidenceFile</strong> only uploads an encrypted, binary image file (using <strong>multipart/form-data</strong> HTTP request header), and does not have a JSON-based request payload.<br><br>Use 'file' as the name of the key that you use to upload the image file. The upload will not be successful if a different key name is used.<br><br>The three image formats supported at this time are <strong>.JPEG</strong>, <strong>.JPG</strong>, and <strong>.PNG</strong>.</span><br><br>After the file is successfully uploaded, the seller will need to grab the <strong>fileId</strong> value in the response payload to add this file to a new evidence set using the <strong>addEvidence</strong> method, or to add this file to an existing evidence set using the <strong>updateEvidence</strong> method. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def upload_evidence_file(payment_dispute_id: str):
    """
    Upload an Evidence File
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/payment_dispute_summary',
    description=""" This method is used retrieve one or more payment disputes filed against the seller. These payment disputes can be open or recently closed. The following filter types are available in the request payload to control the payment disputes that are returned:<ul><li>Dispute filed against a specific order (<b>order_id</b> parameter is used)</li><li>Dispute(s) filed by a specific buyer (<b>buyer_username</b> parameter is used)</li><li>Dispute(s) filed within a specific date range (<b>open_date_from</b> and/or <b>open_date_to</b> parameters are used)</li><li>Disputes in a specific state (<b>payment_dispute_status</b> parameter is used)</li></ul>More than one of these filter types can be used together. See the request payload request fields for more information about how each filter is used.<br><br>If none of the filters are used, all open and recently closed payment disputes are returned.<br><br>Pagination is also available. See the <b>limit</b> and <b>offset</b> fields for more information on how pagination is used for this method. """,
    tags=['dispute_resolution'],
    security=[
        UnsuportedSecurityStub(name="None"),
    ],
)
def get_payment_dispute_summaries(
    order_id: Optional[str] = None,
    buyer_username: Optional[str] = None,
    open_date_from: Optional[str] = None,
    open_date_to: Optional[str] = None,
    payment_dispute_status: Optional[str] = None,
    limit: Optional[str] = None,
    offset: Optional[str] = None,
):
    """
    Search Payment Dispute by Filters
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
