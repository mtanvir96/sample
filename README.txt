# How to run the service
  - git clone  ...
  - docker build -t stats-manager -f Dockerfile .
  - docker run -p 5001:5000 -d stats-manager
  - Run "docker ps" to verify that the container is running

# How to test with Postman
  - Create a GET session to invoke the following URL using 
         http://localhost:5001/metric
  - If need set the content-type=application/text

# How to run the unit test
- Keep the service running using the above instruction

- Create python virtual enviroment to run the unit test
    > pip install virtualenv
    > virtualenv mytest
    > source ../mytest/bin/activate    [May need to run chmod 755]

- Under the virtual environment run following commands
    > pip3 install flask
    > pip3 install requests
    > cd /project/tests
    > python3 -m unittest basic.Testing  (Should see the test output)

# How to deploy using Kubernetes
  - kubectl apply -f deployment.yaml