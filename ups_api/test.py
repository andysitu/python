from access_data import ups_data

import urllib.request, urllib.error

import xml.etree.ElementTree as etree

access_request = etree.Element('AccessRequest',
    attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en-US',})

access_num = etree.SubElement(access_request, 'AccessLicenseNumber')
access_num.text = ups_data.access_license_number

userid = etree.SubElement(access_request, "UserId")
userid.text = ups_data.userid

password = etree.SubElement(access_request, "Password")
password.text = ups_data.password


print(etree.tostring(access_request))

et_access_request = etree.ElementTree(access_request)

et_access_request.write("AccessRequest.xml", 
    encoding='UTF-8', xml_declaration = True)




service_request = etree.Element('RatingServiceSelectionRequest', 
    attrib={'{http://www.w3.org/XML/1998/namespace}lang': 'en-US',},)
request = etree.SubElement(service_request, "Request")

trans_ref = etree.SubElement(request, "TransactionReference")
cust_context = etree.SubElement(trans_ref, "CustomerContext")
cust_context.text = "None"

req_action = etree.SubElement(request, "RequestAction")
req_action.text = "Rate"

req_option = etree.SubElement(request, "RequestOption")
req_option.text = "Rate"

shipment = etree.SubElement(service_request, "Shipment")

rate_info = etree.SubElement(shipment, "RateInformatin")
neg_rate_ind = etree.SubElement(rate_info, "NegotiatedRatesIndicator")

shipper = etree.SubElement(shipment, "Shipper")

ship_name = etree.SubElement(shipper, "Name")
ship_name.text = ups_data.shipper_name
ship_attention_name = etree.SubElement(shipper, "AttentionName")
ship_attention_name.text = ups_data.attention_name
ship_phone_number = etree.SubElement(shipper, "PhoneNumber")
ship_phone_number.text = ups_data.phone_number
ship_num = etree.SubElement(shipper, "ShipperNumber")
ship_num.text = ups_data.shipper_number

ship_address = etree.SubElement(shipper, "Address")
ship_address_line_1 = etree.SubElement(ship_address, "AddressLine1")
ship_address_line_1.text = ups_data.ship_address_line_1
ship_city = etree.SubElement(ship_address, "City")
ship_city.text = ups_data.ship_city
ship_state = etree.SubElement(ship_address, "StateProvinceCode")
ship_state.text = ups_data.ship_state_code
ship_postal_code = etree.SubElement(ship_address, "PostalCode")
ship_postal_code.text = ups_data.ship_postal_code
ship_country_code = etree.SubElement(ship_address, "CountryCode")
ship_country_code.text = ups_data.ship_country_code


shipto = etree.SubElement(shipment, "ShipTo")

shipto_company_name = etree.SubElement(shipto, "CompanyName")
shipto_company_name.text = ups_data.shipto_name
shipto_attention_name = etree.SubElement(shipto, "AttentionName")
shipto_attention_name.text = ups_data.shipto_attention_name
shipto_phone_number = etree.SubElement(shipto, "PhoneNumber")
shipto_phone_number.text = ups_data.shipto_phone_number

shipto_address = etree.SubElement(shipto, "Address")
shipto_address_line_1 = etree.SubElement(shipto_address, "AddressLine1")
shipto_address_line_1.text = ups_data.shipto_address_line_1
shipto_city = etree.SubElement(shipto_address, "City")
shipto_city.text = ups_data.shipto_city
shipto_state = etree.SubElement(shipto_address, "StateProvinceCode")
shipto_state.text = ups_data.shipto_state
shipto_postal_code = etree.SubElement(shipto_address, "PostalCode")
shipto_postal_code.text = ups_data.shipto_postal_code
shipto_country = etree.SubElement(shipto_address, "CountryCode")
shipto_country.text = ups_data.shipto_country


shipfrom = etree.SubElement(shipment, "ShipFrom")

shipfrom_name = etree.SubElement(shipfrom, "Name")
shipfrom_name.text = ups_data.shipper_name
shipfrom_attention_name = etree.SubElement(shipfrom, "AttentionName")
shipfrom_attention_name.text = ups_data.attention_name
shipfrom_phone_number = etree.SubElement(shipfrom, "PhoneNumber")
shipfrom_phone_number.text = ups_data.phone_number
shipfrom_num = etree.SubElement(shipfrom, "ShipperNumber")
shipfrom_num.text = ups_data.shipper_number

shipfrom_address = etree.SubElement(shipfrom, "Address")
shipfrom_address_line_1 = etree.SubElement(shipfrom_address, "AddressLine1")
shipfrom_address_line_1.text = ups_data.ship_address_line_1
shipfrom_city = etree.SubElement(shipfrom_address, "City")
shipfrom_city.text = ups_data.ship_city
shipfrom_state = etree.SubElement(shipfrom_address, "StateProvinceCode")
shipfrom_state.text = ups_data.ship_state_code
shipfrom_postal_code = etree.SubElement(shipfrom_address, "PostalCode")
shipfrom_postal_code.text = ups_data.ship_postal_code
shipfrom_country_code = etree.SubElement(shipfrom_address, "CountryCode")
shipfrom_country_code.text = ups_data.ship_country_code


service = etree.SubElement(shipment, "Service")

service_code = etree.SubElement(service, "Code")
service_code.text = ups_data.service_code
service_description = etree.SubElement(service, "Description")
service_description.text = ups_data.service_description


package = etree.SubElement(shipment, "Package")

packagingtype = etree.SubElement(package, "PackagingType")
packagingtype_code = etree.SubElement(packagingtype, "Code")
packagingtype_code.text = ups_data.packagetype
packagingtype_descpription = etree.SubElement(packagingtype, "Description")
packagingtype_descpription.text = ups_data.packagedescription

packagingweight = etree.SubElement(package, "PackageWeight")
unitmeasurement = etree.SubElement(packagingweight, "UnitOfMeasurement")
unitmeasurement_code = etree.SubElement(unitmeasurement, "Code")
unitmeasurement_code.text = ups_data.unit_measurement_code
weight = etree.SubElement(packagingweight, "Weight")
weight.text = ups_data.weight

dimensions = etree.SubElement(package, "Dimensions")
length = etree.SubElement(dimensions, "Length")
length.text = ups_data.length
width = etree.SubElement(dimensions, "Width")
width.text = ups_data.width
height = etree.SubElement(dimensions, "Height")
height.text = ups_data.height


print(etree.tostring(access_request))

et_service_request = etree.ElementTree(service_request)
et_service_request.write("RatingServiceSelectionRequest.xml", 
    encoding='UTF-8', xml_declaration=True)