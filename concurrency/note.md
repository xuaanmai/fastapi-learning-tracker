- Khi người dùng gọi API, server thực hiện:
Nhận request -> truy vấn DB -> Chờ DB trả KQ -> trả dữ liệu cho client \
Ở bước chờ DB trả KQ, trong thời gian chờ, chương trình có thể phải đợi mà chưa thực hiện được công việc tiếp theo. Nếu có 1000 user cùng gọi API thì việc chờ đợi này có thể lãng phí tài nguyên + giảm khả năng xử lý request.

- Synchronous vs Asynchronous
    + Synchronous: chương trình thực hiện các công việc theo thứ tự
    + Asynchronous: cho phép chương trình tạm dừng một công việc chờ đợi và chuyển sang thực hiện công việc khác. Tận dụng thơi gian chờ để xử lý việc khác

- Concurrency vs Parallelism
    + Concurrency: xử lý đồng thời -> có thể chuyển sang làm một việc khác trong thời gian chờ
    + Parallelism: xử lý song song -> xử lý nhiều CPU hoặc nhiều process để thực hiện nhiều công việc cùng 1 lúc

- I/O-bound vs CPU-bound:
    + I/O-bound: Chương trình dành phần lớn thời gian để chờ dữ liệu từ bên ngoài -> chờ đợi nhiều
    + CPU-bound: Chương trình dành phần lớn thời gian để tính toán bằng CPU -> tính toán nhiều

- async def được sử dụng để khai báo một hàm bất đồng bộ (asynchronous function). Khi được gọi, nó chưa chạy ngay, mà chỉ trả về một đối tượng coroutine (một tác vụ chờ được thực thi). Bên trong hàm, nó có thể sử dụng từ khóa await trước các tác vụ tốn thời gian. Khi gặp await, hàm sẽ tạm dừng và "nhường sân khấu" cho các coroutine khác chạy. Khi kết quả của lệnh await có, nó tiếp tục chạy phần code còn lại.

- await được sử dụng để chờ một coroutine hoặc awaitable hoàn thành và lấy kết quả của nó. Bạn chỉ được sử dụng await bên trong một hàm được khai báo bằng async def.

- asyncio.gather(): nếu muốn 2 tác vụ cùng chờ đồng thời

Ví dụ: 

@app.get("/users/{user_id}") \
async def get_user(user_id: int):

    user = await database.fetch_one(
        "SELECT * FROM users WHERE id = :id",
        values={"id": user_id}
    )

    return user

Khi gặp await:
1. Coroutine tạm dừng để chờ database.
2. Event loop có thể chuyển sang xử lý coroutine khác.
3. Database trả kết quả.
4. Coroutine được tiếp tục.
5. FastAPI trả response về client.