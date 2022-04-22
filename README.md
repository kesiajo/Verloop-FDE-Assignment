# Verloop-FDE-Assignment

When an address is passed in the body, the corresponding latitude and longitude are returned in the response. The format in which the response is returned is dictated by the
`output_format` flag, the options for this flag are “json” or “xml”. If the output flag is set to json the response from the API should be in json format and if the flag
is set to xml the response should be in xml format.

Endpoint: POST /getAddressDetails

Request data
```
{
  "address": "# 3582,13 G Main Road, 4th Cross Rd, Indiranagar, Bengaluru, Karnataka 560008",
  "output_format": "json"
}
```

