for i in {1..50}; do \
    curl -X 'POST' \
    "http://localhost:8000/send-message?message=$i" \
    -H 'accept: application/json' \
    -d ''
done