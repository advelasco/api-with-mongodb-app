# Python Rest API with MongoDB

Creating Rest API with Python and MongoDB

#### First you need to creat your envinroment (I'm using Anaconda and PyCharm)
`$ mkdir api-with-mongodb-app`

`$ conda create -n api-with-mongodb-app`

`$ conda activate api-with-mongodb-app`

`$ conda install pymongo`

`$ conda install flask`

`$ conda install flask-restful`

#### Setup your MongoDB
    self.client = MongoClient("127.0.0.1", 27017)

#### Just Run using your own approach or IDE and play around

#### How to test the API's
> curl --noproxy "*" http://127.0.0.1:5000 -X GET -v

> curl --noproxy "*" http://127.0.0.1:5000/category -X POST -d "name=Category" -v

> curl --noproxy "*" http://127.0.0.1:5000/category -X GET -v

> curl --noproxy "*" http://127.0.0.1:5000/category/name/{CATEGORY_NAME} -X GET -v

> curl --noproxy "*" http://127.0.0.1:5000/category/{CATEGORY_ID AS GUID} -X GET -v

> curl --noproxy "*" http://127.0.0.1:5000/category/{CATEGORY_ID AS GUID} -X DELETE -v

