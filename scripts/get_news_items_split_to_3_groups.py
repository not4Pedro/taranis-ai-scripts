import json

group_1 = [
    "6481b5cd-9843-42a5-b17c-a492e5aeca91",
    "93f68927-0573-44dd-b3ba-9437123d662c",
    "fefdac46-a96a-4b52-8bc7-afdd1b6f1240",
    "8185fdd1-d021-439f-a6dc-8b04ebc9aeed",
    "a9981bcb-978a-4a82-89f4-9bf5d3fd6d0a",
    "cc101f4b-dc02-452b-a934-73b2442e0452",
    "5583d5bf-4e21-48d8-8432-65c40c35637e",
    "0816fa48-ab7a-40cf-9712-c5e55eca7fa3",
    "3356ab60-4903-498a-901d-23b2417fd473",
    "616f2ce2-8f45-4f60-810a-1931cc42945a",
    "41d7b6df-6033-4589-a473-d0ed73a99d60",
    "3df3afe2-c16a-4aa3-8a9d-d67437b86a2a",
    "0cc6ae58-702a-4761-a325-fa8d57957db2",
    "c207add4-d55f-4cca-8e7d-f8d28dba3147",
    "1234d68d-a6a4-4dff-ab66-8a4fc58a4ee1",
    "40eef211-9cd2-4965-967c-355192502085",
    "d701e112-1749-4777-b39e-5b36b202c254",
    "4e51f021-addf-4a5e-9922-0bbfc42b9504",
    "957579b1-91d2-4035-9517-5c9f2ec71853",
    "de168845-d411-4719-8acc-bbb114254b5d",
    "118307f7-b82c-4118-a72c-bbb37d3840cc",
    "52c0892e-bbd4-4d71-8bd2-35c0afab8357",
    "6b31d655-a2e0-4d18-ae1a-503bb5a16444",
    "0de48c2c-9527-46bb-9a44-444ee0910ea9",
]

group_2 = [
    "fd01c2d3-1394-4d61-9258-97a5f68d4166",
    "813adf5c-3843-48ab-9ef2-aef282c7629e",
    "cd807dcb-9304-48f6-a0fb-6a741aa07afc",
    "6a906578-c364-4519-bed1-3102083c8dcf",
    "272b0a8c-8464-442b-89cf-22e9cfc84337",
    "76ac2a5b-c4f8-45b7-8243-73f4032bbb1a",
    "703c360b-8a01-4f16-9a5d-1a00df8fdaea",
    "f8debe60-f62b-4150-9eee-0fba49cff3c1",
    "e20d38b8-2a9d-48a2-82c9-551f6e4c001f",
    "cbad64bc-fc3b-4780-87cd-513212617451",
    "e12f2003-e370-4354-902d-0be488061e2a",
    "7810c0a1-0350-4415-bd54-c2b0f98be334",
    "3525082c-19f6-4ef1-a1e2-150d63632878",
    "bdaf5994-07d1-4049-9789-a4ae2eecd7f0",
    "19d0d378-4b46-41cf-9648-640a17cb02d7",
    "5c9092ce-3b7f-47ac-a77d-49fb415b6653",
    "479d5ae3-74ee-423f-aeb7-fa443fe59f82",
    "3961c75c-e3d7-4bed-91cc-8943a6a6a63e",
    "cc499ee2-f07e-4864-be2d-4e3adc62b9ce",
    "e2b47244-fdff-4970-a031-83fd309e7989",
    "fbae9255-206f-4681-9f15-ee7f4dbed9be",
    "85631a9d-bbe8-4590-8aeb-307e6fc9a2b7",
    "cf0d8f5a-76b3-4d7c-84c5-b616606bae5d",
    "0de48c2c-9527-46bb-9a44-444ee0910ea9",
]

group_3 = [
    "27bb3688-0e50-473d-9aea-9ed545245918",
    "cc0166b2-7f44-401e-9073-3619286b3c05",
    "677fa710-4a63-4dde-b673-f56d1dd684e2",
    "e13f0f45-ec64-4a55-8795-8387816f0772",
    "2fe06fdc-46a6-4688-ba01-3f0931aab7a5",
    "af54dfde-ac1b-4fa2-9db0-0cc7e12a248e",
    "25518aad-1da6-483c-9ce1-e1d977936ce6",
    "d2995655-6c82-4bdc-8cbc-6fc817ab2f44",
    "bc6033e2-a20b-4773-967c-dd56be679eb9",
    "d0ca5655-5f43-4d3c-87dc-031275abb6d1",
    "a2216e8a-c411-4949-86ec-6b6849f4d879",
    "4381bba9-7b0b-4903-b89d-9894275d3155",
    "b4303fe2-7fe6-4022-898c-7ad46a8fea23",
    "4b16b707-63bc-44f8-87d6-dfc0e9ac1aef",
    "2b100679-c794-4e46-9745-9a01b17242ce",
    "5eef78e1-8c5d-41fb-a271-b848c08946a7",
    "5695495b-25ad-4d8c-9c5c-10bb493e0672",
    "933e8348-2ec1-4acd-961f-d4653f237789",
    "df6cd389-7748-4768-a999-b2541fe3a275",
    "5aad1a10-74c6-47d4-ad23-7945d84835ca",
    "bbab31ad-5ccd-45e2-897a-49fae32a796c",
    "8f10d294-a1fd-4ee1-80dd-5901be5e827c",
    "f41d436f-f47c-4f84-8390-59c04eca0a2a",
    "dce267fa-6311-45ed-a65c-dd3e988aac26",
    "0de48c2c-9527-46bb-9a44-444ee0910ea9",
]


def extract_group_stories(input_file, output_file, group_sources):
    with open(input_file, "r") as infile:
        stories = json.load(infile)

    filtered_stories = [
        story
        for story in stories
        if story.get("source_id") in group_sources and "news_items" in story
    ]

    with open(output_file, "w") as outfile:
        json.dump(filtered_stories, outfile, indent=2)


# Example usage
extract_group_stories("all_stories.json", "group_1_stories.json", group_1)
extract_group_stories("all_stories.json", "group_2_stories.json", group_2)
extract_group_stories("all_stories.json", "group_3_stories.json", group_3)
