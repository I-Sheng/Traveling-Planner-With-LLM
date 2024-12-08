curl -X POST http://localhost:5002/routing \
-H "Content-Type: application/json" \
-d '{
  "day": 1,
  "sites": "嘉義市環市自行車道, 嘉義市立博物館, 嘉義文化創意產業園區, 嘉義公園, 嘉義市史蹟資料館, 上島咖啡, 七彩冰果室, 舊時光新鮮事, 燒肉觀止"
}'
