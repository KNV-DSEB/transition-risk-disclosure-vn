# Trích xuất và kiểm chứng thông tin rủi ro chuyển đổi có dẫn chứng

Đề tài: *Xây dựng và đánh giá hệ thống LLM có dẫn chứng để trích xuất và kiểm chứng thông tin rủi ro chuyển đổi từ báo cáo công bố của doanh nghiệp niêm yết Việt Nam.*

**Trạng thái (22/10/2026):** đề xuất v1.0, chờ supervisor góp ý và nhóm phê duyệt. Chưa có dữ liệu thu thập hay code pipeline; việc tiếp theo là Pha 0.

## Đọc gì trước

1. [`docs/De_xuat_de_tai_v1.0.docx`](docs/De_xuat_de_tai_v1.0.docx): toàn bộ đề xuất, gồm bối cảnh, tính mới, khoảng trống, dữ liệu, cách thu thập, mô hình, luồng xử lý, đánh giá, lộ trình, rủi ro và các quyết định cần duyệt.
2. [`docs/DATASET_CATALOG.md`](docs/DATASET_CATALOG.md): các bộ dữ liệu công khai dùng để huấn luyện thành phần, kèm license và trạng thái xác minh.

## Cấu trúc thư mục

| Đường dẫn | Nội dung |
|---|---|
| `docs/De_xuat_de_tai_v1.0.docx` | Đề xuất đề tài (bản bàn giao) |
| `docs/DATASET_CATALOG.md` | Danh mục dữ liệu công khai |
| `CONTEXT_FACT_REGISTER.md` | Dữ kiện pháp lý về thị trường carbon Việt Nam đã kiểm chứng, kèm mức độ xác minh (tiếng Anh) |
| `GLOSSARY_VI_EN.md` | Thuật ngữ Việt–Anh |
| `DATA_PROVENANCE_PROTOCOL.md` | Quy tắc lưu trữ, định danh và truy vết nguồn dữ liệu (tiếng Anh) |
| `SOURCE_MANIFEST.csv` | Sổ đăng ký nguồn: mỗi file tải về có một dòng gồm URL, ngày tải, sha256 |
| `scripts/lit_search.py` | Tìm văn liệu có ghi log (OpenAlex, Crossref, kiểm tra DOI) |
| `scripts/inspect_fulltext.py` | Tìm đoạn trích có số trang trong PDF toàn văn |

Một số tài liệu nền được kế thừa từ giai đoạn trước của dự án, nên có thể nhắc tới tài liệu nội bộ không có trong nhánh này. Các dòng có sẵn trong `SOURCE_MANIFEST.csv` là nguồn pháp lý của giai đoạn trước; nguồn mới được thêm tiếp vào cùng file.

## Quy tắc dữ liệu (bắt buộc)

- **Không commit PDF** báo cáo doanh nghiệp hay toàn văn bài báo, vì lý do bản quyền. `.gitignore` đã chặn `data/raw/**/*.pdf` và `literature/fulltext/`.
- Dữ liệu thô trong `data/raw/` không được sửa. Mọi xử lý ghi sang thư mục khác.
- Mỗi file tải về phải có một dòng trong `SOURCE_MANIFEST.csv`.
- Khi tải: tuân thủ robots.txt và điều khoản sử dụng, giãn cách ≥ 3 giây mỗi request, không vượt captcha hay trang đăng nhập.
- Không đưa khóa API vào repo. Dùng file `.env`, đã được `.gitignore` chặn.

## Cách dùng script

```bash
# Tìm văn liệu (lưu phản hồi thô vào literature/search_runs/, mỗi SEARCH_ID chỉ dùng một lần)
python scripts/lit_search.py <SEARCH_ID> openalex "<truy vấn>" --from-year 2020 --n 25
python scripts/lit_search.py <SEARCH_ID> doi <doi>

# Tìm đoạn trích theo regex trong một PDF toàn văn (file lưu ở literature/fulltext/, không commit)
python scripts/inspect_fulltext.py <PAPER_ID> <url-pdf> "<regex1>" "<regex2>"
```

Cần Python 3.10+. `lit_search.py` chỉ dùng thư viện chuẩn; `inspect_fulltext.py` cần thêm `pymupdf` (`pip install pymupdf`).

## Việc tiếp theo (Pha 0)

- [ ] Supervisor góp ý; nhóm ra quyết định chính thức về đề tài.
- [ ] Tìm người gán nhãn thứ hai (bắt buộc để đo κ).
- [ ] Kill-paper hunt toàn văn cho các công trình ở mục 3.1 của đề xuất.
- [ ] Đếm số doanh nghiệp niêm yết trong khung mẫu; lập `targets.csv`.
- [ ] Soạn taxonomy v0 và hướng dẫn gán nhãn v0.
- [ ] Chốt ngưỡng Cổng 1, gồm tiêu chí mật độ.
- [ ] Viết `scripts/fetch_reports.py` (tải báo cáo và ghi manifest).
