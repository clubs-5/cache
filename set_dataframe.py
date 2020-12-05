import pyarrow as pa
import redis

# 準備 redis
r = redis.Redis(host='master.tibame', port=6379, db=0)

# 序列化 pandadf
df_compressed = pa.serialize(pandadf).to_buffer().to_pybytes()

# 建立 redis key 'recomm' 並寫入
res = r.set('recomm',df_compressed)
