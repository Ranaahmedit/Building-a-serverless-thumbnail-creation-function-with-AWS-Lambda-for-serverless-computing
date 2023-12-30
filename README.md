# Building a serverless thumbnail creation function with AWS Lambda for serverless computing

# Task 1: Creating Two Amazon S3 Buckets:

Create an Amazon S3 bucket for uploading images.
Create another Amazon S3 bucket for storing resized thumbnail images.
Understand the configuration settings for storing files in an S3 bucket.

# Task 2: Creating Permissions Policies for Lambda:

Understand the concept and significance of policies in AWS.
Create an IAM policy allowing Lambda to read and write inside the S3 buckets.
Grant permissions in the policy for Lambda to write to Amazon CloudWatch Logs.

# Task 3: Creating Execution Role:

Understand the importance of roles within AWS.
Associate the permissions policy with the Lambda service.

# Task 4: Creating Permissions Policies for S3 Buckets:

Create a policy allowing Lambda to read from the S3 bucket.
Create a policy allowing Lambda to write inside the S3 bucket.

# Task 5: Creating the Code Package:

Understand how to work with programming packages.
Write code responsible for resizing images using Python.

# Task 6: Creating the Lambda Function:

Create a Lambda function, specifying the programming language used.
Upload the code responsible for resizing images to the Lambda function.

# Task 7: Configuring Lambda to Trigger on S3 Bucket Events:

Understand how to invoke Lambda on specific events.
Explore different events within Lambda settings.
Configure Lambda to operate when images are uploaded to the S3 bucket.

# Task 8: Testing Lambda Function by Adding an Image to Amazon S3 Bucket:

Add an image file to the S3 bucket.
Trigger the Lambda function.
Verify the functionality of the image resizing code.


