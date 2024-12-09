curl -X POST http://localhost:5001/recommend \
-H "Content-Type: application/json" \
-d '{
  "day": 1,
  "preference": "美食之旅"
}'
