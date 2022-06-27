
# polarity

- 1 = positive
- -1 = negative

following
https://towardsdatascience.com/the-nice-way-to-deploy-an-ml-model-using-docker-91995f072fe8

control shift P
add docker file
it creates it, just build it

    Executing task: docker-build <

    > docker build --rm --pull -f "C:\Users\spage\Documents\py\polarity/Dockerfile" --label "com.microsoft.created-by=visual-studio-code" -t "polarity:latest" "C:\Users\spage\Documents\py\polarity" 

run it

    > Executing task: docker run --rm -d  -p 8000:8000/tcp polarity:latest <

test it

    POST localhost:7000/predict
    {"text":"These shoes are great, styling and a comfy fit"}
    ===
    {
        "polartiy": 0.6000000000000001,
        "subjectivity": 0.575
    }
