from google.cloud import pubsub_v1
import json

publisher = pubsub_v1.PublisherClient()

def hello_firestore(event, context):
    """Triggered by a change to a Firestore document.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    resource_string = context.resource
    # print out the resource string that triggered the function
    print(f"Function triggered by change to: {resource_string}.")
    # now print out the entire event object
    print(str(event))
#projects/test-function-project-384218https://github.com/emmaajebit/CloudFireStore_PubSub_integration/blob/main/main.py16/topics/demo-pub
    topic_name = 'demo-pub'
    PROJECT_ID =  'test-function-project-384218'
    message = str(event)

    topic_path = publisher.topic_path(test-function-project-384218, demo-pub)

    message_json = json.dumps({
        'data': {'message': message},
    })
    message_bytes = message_json.encode('utf-8')

    # Publishes a message
    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return 'Message published.'
    except Exception as e:
        print(e)
        return (e, 500)
