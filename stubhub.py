import requests
import json

url = "https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2"

payload = {}
headers = {
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
  'content-type': 'application/json',
  'cookie': '_rvt=rFbRZQHQbcqxxKL2gdxiv6bJR12mKkQoiMVd03FTPlos_rVQvH_YOLFKYPg1djcEadESpZ3uRL91w3vBYDH2FkDw_iFwemi_hpsIePbWg141; d=ihkPpemC3QESKFpYN6esTq1TfXNPK4QKKUXH7w2; s=MOH4I8QepUey4CS7HQRGqONc-dVdE90I0; ak_bmsc=F03A839ED1854E524D83097B527FF6AB~000000000000000000000000000000~YAAQv/XSF8wFhS2TAQAAvkwOixktCzMlptDQPQ8nvGs7W+jlLzazJWOuvAS9fOB9flb65TOULrqkcSL718yXtDsYfnz+p57RXr4UjjEb9ddaoZYyk6r7VbrH73RPjXSZXD20pRStGq5gYNOGUG/iJsam81679Q5WyCa5O763MfdbNQ+vgQm4av8cSkn9zNsZH1QMVLeQdBf8uG8QZZ0DhR9YDXS1ZQeXKYCnnpi8yABpmQ3eqJ1637CIlcgs96Lrvl6yEqZVELPyyxqSkiEfirL6hi6KkYp5fcpyDIRkQIpMxl0g1F42gCYypL6QtwFKVokJyaagH8ialUDSSNo200/1cSztYrfmnhSeJT6x2BOm83n3y1ZNuIoSUME0KYHcNBVqtBYdAmTfKkY+; auths=0; ai_user=Qt2d3ZKDECu3pBSlTan8Fw|2024-12-03T05:46:33.651Z; _gcl_au=1.1.1569648514.1733204795; wsso-session=eyJ1bCI6bnVsbCwidXBsIjp7ImN0IjoiVVMiLCJuIjoiRmxvcmlkYSUyMENpdHkiLCJsdCI6MjUuNDQ3ODg5OCwibGciOi04MC40NzkyMjM2OTk5OTk5OSwic3JjIjoiUVVFUllfUEFSQU0ifSwiZCI6bnVsbCwicnYiOnsiYyI6W10sImUiOltdLCJsIjpbXSwicnRjX3UiOm51bGwsInJ0Y19ldCI6IjIwMjQtMTItMDNUMDU6NDY6MzMuNjYwNzI3NVoifSwiZmMiOnsiYyI6W119LCJwIjpbXSwiaWQiOm51bGx9; _ga=GA1.1.1837478951.1733204795; _abck=97F143A0C5F7C940C7BDECB6E7D13841~0~YAAQv/XSFyrtiy2TAQAAN1Qliwy903aezjmU9JoWHkzqQOTCxJbKZi7y7UXpeZoRQHZ4VzEEMj03bCbvrwCm4ehQVZ6pkaswh0j4Vn3bDmSIeMqHo8Q6raTlgjXqAxIK3oqcJ4EO1Uao3B0Mik9ig9Jm/tNMsJyKJCnPAw+L9Xg/uoK0JeCnaWq7uS09Ekv8pn143M13KG+IFWY+z49dZnhXdKUJyM2JNin3cWJUbUzqEYIuAxc/kW6QyjLF9AwaxdwscTH6IvSs5jGF18dfbXR7HenaKl0n4TWpCUXnkyE+Eoj0AcLjPovpkkCEwK53g2ZqbcJZ0YVBnRvVXeNeg4gI+NnEPn7mqiibegdwj1xGGc65vy9FT4RYidxDoHJKa8DiIM+xVPpCHZ7tbZBvhT/G6FWdCBK9/gUaexcI5bEmOHrNxCgoi3O+hU89IxgAdYaRy+/slS/mlOtDsyrzVoe+mU/d1TYGGNyWfTukL1sJ~-1~-1~-1; bm_ss=ab8e18ef4e; bm_s=YAAQNnLBF/MLtm+TAQAAXsMviwIbFV2+yT1UimSueldsmg6sdOy7N4EXFTpmtulVMDpUnD98OoRuJ3vAfNRgOanSLmRpqLhq/K9nGz9oLy7TyX14xzZpy+duvpG0LnGTG/02VwPlC+s9PItcEJM16e6JbMk7EKDt1QxinxWwKPk2z+Ic7VZm+jlEvlkEPC6PtpQn/Wj4q29ZhS5Hi3MK9GRZusGREi11zLlypekytb53/bjxenYm/Ev9vv3VK4C5Amfu0oz3daFp42zBjpHyJQ5VJGlMMoGISEIQtF33eebGQ0Cvb13vHB/ojs+co0lbfAjNRh4tn12ASlm+bmHxRBUFIvPOU1Y=; bm_so=307EE20B96DCDAED97B613535BDA1B5EBBFC81E1ABB9BB2AC53DA2D53750FC0B~YAAQNnLBF/QLtm+TAQAAXsMviwGzu3dVzuHXsqdKM5I4hpzemJXYxU6goAF3mwITRM/SvTHLXpjbG+xHC3aMlH8BxDkTGB+VtV7jL33Z+E/qfDhFTdqyYVx9X2Jl9qoIKD7FSY8v62XZlVeEP6uRNGPXJ82cRvQ8xUflX/tWRUX0hkOz5D467MF+lQGTb6xEOD2loKwlozIhFD/32prJcdNhJJD3Y/Bb9tZzhg2X5G6GsXQbUjtIANdwoJwYUwSNtpRNsFl4StB4RhZtk8MLd/TBVFMmIfqmaDCIvlJ+58YHby3v8b00FbWvPXb8jwx+PeL1mL0EFMYKWbLCz/CN3T1piglqLsvkI2QxSdzVlzw8re6CmZwWAoMZNvsA1eVYE0RDy291IyeeMGAmhnwdhNRLq+hhhLvxW5rdI9A1XPNRZxIBSF4JmwKSz4g5JFCrsoNpJefsOh7E1z2D3JrBDQ==; bm_lso=307EE20B96DCDAED97B613535BDA1B5EBBFC81E1ABB9BB2AC53DA2D53750FC0B~YAAQNnLBF/QLtm+TAQAAXsMviwGzu3dVzuHXsqdKM5I4hpzemJXYxU6goAF3mwITRM/SvTHLXpjbG+xHC3aMlH8BxDkTGB+VtV7jL33Z+E/qfDhFTdqyYVx9X2Jl9qoIKD7FSY8v62XZlVeEP6uRNGPXJ82cRvQ8xUflX/tWRUX0hkOz5D467MF+lQGTb6xEOD2loKwlozIhFD/32prJcdNhJJD3Y/Bb9tZzhg2X5G6GsXQbUjtIANdwoJwYUwSNtpRNsFl4StB4RhZtk8MLd/TBVFMmIfqmaDCIvlJ+58YHby3v8b00FbWvPXb8jwx+PeL1mL0EFMYKWbLCz/CN3T1piglqLsvkI2QxSdzVlzw8re6CmZwWAoMZNvsA1eVYE0RDy291IyeeMGAmhnwdhNRLq+hhhLvxW5rdI9A1XPNRZxIBSF4JmwKSz4g5JFCrsoNpJefsOh7E1z2D3JrBDQ==^1733206985505; ulv-ed-event={"155472128":[1733206985751]}; _fbp=fb.1.1733206987295.19731459745033406; lastRskxRun=1733206987490; rskxRunCookie=0; rCookie=5xn2ob5gfccax7y818vfknm482oulh; ai_session=UF69+SvnGJkJHs0WjfZMJX|1733206989572|1733206989572; forterToken=364e7c0aa8ff4609bf78119489b6926d_1733206985897__UDF43-m4_24ck_1EbAtY03PYU%3D-592-v2; forterToken=364e7c0aa8ff4609bf78119489b6926d_1733206985897__UDF43-m4_24ck_1EbAtY03PYU%3D-592-v2; wsso=eyJ1bCI6bnVsbCwidXBsIjp7Im4iOm51bGwsInMiOmZhbHNlLCJsZyI6MC4wLCJsdCI6MC4wLCJjdCI6bnVsbCwic3JjIjoiREVWSUNFIiwiZHQiOiIwMDAxLTAxLTAxVDAwOjAwOjAwKzAwOjAwIn0sImQiOnsidHlwZSI6MCwiZGF0ZXMiOnsiZnJvbSI6bnVsbCwidG8iOiI5OTk5LTEyLTMxVDIzOjU5OjU5Ljk5OTk5OTlaIiwiZXhwaXJhdGlvbiI6bnVsbH19LCJydiI6eyJjIjpbXSwiZSI6W3sidCI6IjIwMjQtMTItMDNUMDY6MjM6MDMuMjA0NTQzOFoiLCJpZCI6MTU1NDcyMTI4fV0sImwiOltdLCJydGNfdSI6bnVsbCwicnRjX2V0IjoiMjAyNC0xMi0wM1QwNTo0NjozMy42NjA3Mjc1WiJ9LCJmYyI6eyJjIjpbXX0sInAiOltdLCJpZCI6bnVsbH0=; _uetsid=f4b281a0b13911efaceb918da1286b0d; _uetvid=f4b27090b13911ef95a689558ee9d035; bm_sz=63C1096698A1CE9AF19DABF79DE4B532~YAAQt/XSF+jbdzGTAQAA9QkzixmUQUitXQqr8u5/7VMbSzM1SIiqokmL4PWu5H/musWnFycp6tAvY6j+NueKMkGP/sXmAQXm+Vdsqr+1laoZZIlqQ1i86hfJ9kXWNnKnXReYj7V9kd0ElluWERSQjKo8oZOQjKxmkXQL9Q+i4dDMV05SEloTIpk8PtYRUBMNBcMwE0ErygoEDPkrIzmff02Oz+Caz8YJqTpJcST4qdmr6BveyOAPeRngyjNbM44p0bpP3fayONRxqM5jUQ7jhRVf99jXsSGZtXb0ZMvocoSeUj5kyUCNiRllRwZQfLoDfchLA9Vh/rGCtEwX9zc1VgDPPB0/0fqLTyJOM/xk02lXoCLCq4yS1dMX4gCcBx2R2VN835mdUEdmsW2YAt8VFneZzuZHOGVng5FAz4DeBmEC3pdv8wJj7bLDkMEPhkzqyIzBFlYYJPjuSHpwMYyatI0q6TgHRXCv~3551302~3488050; _ga_1686WQLB4Q=GS1.1.1733204795.1.1.1733207198.0.0.0; akacd_rls=1733228799~rv=70~id=97a1af0170643c40fd6b5562b616b880; _abck=97F143A0C5F7C940C7BDECB6E7D13841~-1~YAAQv/XSF9djky2TAQAAYks7iwxIUtz7mAjKS7lQ47B54x2+RnCq/9orbvJjK1fVFbp/MI1fuLPiNh+WluKZpSze5XISlVBM7vTqkp9Ao7B3HSgNAxdDEtOfPyAJLXARfMblwPNOmVBrdPQXcA6Iwy+DvnrdUeeRDU02maBkCqoZbJf9qQ4A12f8TrHKC/9wwCKm8SQR+/0TwkDSrUz0KyijhYRQhaFKhlTDIKpONm9W2un+WcK2HV7ChCHTr4Ob8dk2ahWfYkIm3Ru/VfZZ0RKP57HiQzvBuRuGKmwsOrfE6ZXAfNesoDHNKTipSTYUXVD75QgbURxTw/FpWr0nreZukR/iYEC6l/+QZQSSb2Ji/wyCb85ma4MKXb84UC/nyf/8/eZedbHZD0G9+CuXUJ3Fd4mxMNbux9Fur+m8AJeI7xfSIyWYyJSXfnW9mDBprYiqxtZudZN7JmwJ3T4R/QWxwFD4ugVdzI1QnpybhWPM~0~-1~-1; akacd_rls=1733229339~rv=70~id=0eec47d1bc207fe53761e902281bda2a',
  'priority': 'u=1, i',
  'referer': 'https://www.stubhub.com/explore?lat=MjUuNDQ3ODg5OA%3D%3D&lon=LTgwLjQ3OTIyMzY5OTk5OTk5&to=253402300799999&tlcId=2',
  'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
res = response.json()

# saving file in Json
with open("event.json", "w") as outfile:
    json.dump(res['events'], outfile)

res['events']

