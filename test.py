data=[
  {
    "asset_id": 100000002711650.0,
    "byline": "By ELI J. FINKEL",
    "des_facet": [
      "MARRIAGES",
      "DIVORCE, SEPARATIONS AND ANNULMENTS",
      "SOCIAL CONDITIONS AND TRENDS",
      "SOCIOLOGY"
    ],
    "title": "The All-or-Nothing Marriage",
    "url": "http://www.nytimes.com/2014/02/15/opinion/sunday/the-all-or-nothing-marriage.html",
    "media": [
      {
        "media-metadata": [
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-thumbStandard.jpg",
            "width": 75,
            "height": 75,
            "format": "Standard Thumbnail"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-superJumbo.jpg",
            "width": 2048,
            "height": 1552,
            "format": "superJumbo"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-sfSpan.jpg",
            "width": 395,
            "height": 263,
            "format": "Large"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-thumbLarge.jpg",
            "width": 150,
            "height": 150,
            "format": "thumbLarge"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-articleInline.jpg",
            "width": 190,
            "height": 144,
            "format": "Normal"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-square640.jpg",
            "width": 640,
            "height": 640,
            "format": "square640"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-square320.jpg",
            "width": 320,
            "height": 320,
            "format": "square320"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16COVER/16COVER-mediumThreeByTwo210.jpg",
            "width": 210,
            "height": 140,
            "format": "mediumThreeByTwo210"
          }
        ],
        "subtype": "photo",
        "type": "image",
        "copyright": "Pieter Van Eenoge",
        "caption": ""
      },
      {
        "media-metadata": [
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-thumbStandard.jpg",
            "width": 75,
            "height": 75,
            "format": "Standard Thumbnail"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-superJumbo.jpg",
            "width": 2048,
            "height": 1815,
            "format": "superJumbo"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-sfSpan.jpg",
            "width": 395,
            "height": 263,
            "format": "Large"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-thumbLarge.jpg",
            "width": 150,
            "height": 150,
            "format": "thumbLarge"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-articleInline.jpg",
            "width": 190,
            "height": 168,
            "format": "Normal"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-square640.jpg",
            "width": 640,
            "height": 640,
            "format": "square640"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-square320.jpg",
            "width": 320,
            "height": 320,
            "format": "square320"
          },
          {
            "url": "http://graphics8.nytimes.com/images/2014/02/16/sunday-review/16MARRIAGEJP/16MARRIAGEJP-mediumThreeByTwo210.jpg",
            "width": 210,
            "height": 140,
            "format": "mediumThreeByTwo210"
          }
        ],
        "subtype": "photo",
        "type": "image",
        "copyright": "Pieter Van Eenoge",
        "caption": ""
      }
    ],
    "section": "Opinion",
    "views": 1,
    "id": "100000002711649",
    "column": "Opinion",
    "geo_facet": "",
    "adx_keywords": "Marriages;Divorce, Separations and Annulments;Social Conditions and Trends;Sociology",
    "source": "The New York Times",
    "org_facet": "",
    "published_date": "2014-02-16",
    "per_facet": "",
    "type": "Article",
    "abstract": "Couples can be happier now than ever before. But it\u2019s rare."
  }]

title=[]
for item in data:
    title.append({'section':item['title']})

    for key in item:
        if key=='media':
            for values in item[key]:
#                print values
                for urls in values['media-metadata']:
                    if urls['format']=='Standard Thumbnail':
                        print urls['url']
