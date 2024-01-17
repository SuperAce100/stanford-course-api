# Stanford Courses REST API
Easily queriable REST API for the Stanford ExploreCourses catalog of courses. 

To use the API, simply submit an HTTP GET request to this URL: `https://courses-kjatbvspvq-ue.a.run.app/getjson?q=YOUR_QUERY`

## Parameters

### Query
Format your query as the course code of your course, i.e. CS106B or MATH51. This parameter is required.

### Multiple
The API defaults to returning one course with an exact match, but can also return multiple courses including prereqs. Set the multiple tag to true enable multiple responses.

## Examples
`https://courses-kjatbvspvq-ue.a.run.app/getjson?q=CS103`
`https://courses-kjatbvspvq-ue.a.run.app/getjson?q=CS106&multiple=true`
