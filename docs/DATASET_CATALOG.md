# DATASET CATALOG — dữ liệu công khai cho các thành phần của pipeline

Phiên bản: 1.0 · Ngày: 2026-10-22 · Kèm theo: `docs/De_xuat_de_tai_v1.0.docx` (mục 5.4)

Chưa có bộ dữ liệu công khai nào khớp đúng bài toán: tiếng Việt, rủi ro chuyển đổi, trích xuất theo trường, kiểm chứng mức đủ của bằng chứng. Các bộ dưới đây chỉ dùng để **huấn luyện thành phần** (verifier, baseline, mô hình bảng) và **chạy thử pipeline**. Chúng không thay tập kiểm tra tự gán nhãn của nhóm.

Cột "Xác minh" ghi những gì đã được kiểm tra ngày 19–22/10/2026 bằng web search và đọc trang nguồn. "Chưa xác nhận" nghĩa là phải đọc dataset card hoặc điều khoản trước khi dùng.

## A. Phân loại đoạn văn khí hậu / rủi ro (baseline)

| Bộ dữ liệu | Nội dung | Dùng cho | Truy cập | License | Xác minh |
|---|---|---|---|---|---|
| ClimateBERT datasets: `climate_detection`, `climate_sentiment`, `climate_specificity`, `climate_commitments_actions`, `tcfd_recommendations`, `environmental_claims`, `netzero_reduction_data` | Câu/đoạn từ báo cáo thường niên, báo cáo bền vững, earnings call. Nhãn: liên quan khí hậu, rủi ro/cơ hội, độ cụ thể, cam kết/hành động, nhóm TCFD | Baseline phân loại; tham khảo nhãn mức cam kết | https://huggingface.co/climatebert | CC BY-NC-SA 4.0 đã xác nhận cho `climate_detection`, `climate_commitments_actions`, `environmental_claims`; các bộ khác cần xem card | Danh sách 7 bộ đọc trực tiếp từ trang tổ chức |
| ClimaText | Câu từ web, Wikipedia và phần rủi ro khí hậu trong 10-K; nhãn liên quan khí hậu hay không | Lọc đoạn liên quan khí hậu | Trong ClimaBench | Chưa xác nhận | Chưa có link Hugging Face chính thức |
| Climate-Eval (ClimateNLP 2025) | Tổng hợp 25 task từ 13 bộ dữ liệu | Đánh giá nhanh LLM zero/few-shot | https://arxiv.org/abs/2505.18653 | Theo từng bộ con | Mức tóm tắt |

## B. Truy xuất bằng chứng từ báo cáo (retriever / RAG)

| Bộ dữ liệu | Nội dung | Truy cập | License | Xác minh |
|---|---|---|---|---|
| ClimRetrieve (EMNLP 2024) | 30 báo cáo bền vững, 16 câu hỏi, hơn 8.500 cặp câu hỏi–nguồn–trả lời có mức liên quan | https://arxiv.org/abs/2406.09818 | Bài báo CC BY-NC-SA 4.0; license dataset chưa xác nhận | Tên bài đã xác nhận; link tải dữ liệu không có trên trang arXiv |
| Climate Finance Bench (2025) | 33 báo cáo, 330 cặp QA (trích xuất, tính toán, suy luận) | https://github.com/Pladifes/climate_finance_bench | Không ghi trên trang dự án | Link GitHub đọc từ trang dự án |
| ESGBench (ICAIF 2025 workshop) | QA có bằng chứng nguyên văn, cache bảng; khoảng 119 QA từ 12 báo cáo (nguồn thứ cấp) | https://github.com/sherinegeorge21/ESGbench | Chưa xác nhận | Quy mô chưa đối chiếu với repo |
| ChatReport (EMNLP 2023 demo) | Dữ liệu gán nhãn và phân tích TCFD của 1.015 báo cáo | https://arxiv.org/abs/2307.15770 | Chưa xác nhận | Mức tóm tắt |
| LobbyMap (NeurIPS 2023 D&B) | Khoảng 10K tài liệu doanh nghiệp; trang bằng chứng, 13 nhóm chính sách, lập trường | https://climate-nlp.github.io | **Bản quyền thuộc InfluenceMap** (theo bài báo) | Đã đọc bài báo; pipeline PDF của nhóm tác giả dùng docTR + PyMuPDF |

## C. Kiểm chứng (verifier NLI / claim–evidence)

| Bộ dữ liệu | Nội dung | Truy cập | Xác minh |
|---|---|---|---|
| CLIMATE-FEVER | 1.535 claim khí hậu, mỗi claim 5 câu bằng chứng Wikipedia; SUPPORTS / REFUTES / NOT ENOUGH INFO | https://arxiv.org/abs/2012.00614 | Mức tóm tắt |
| ViNLI (COLING 2022) | Hơn 30K cặp premise–hypothesis tiếng Việt từ báo điện tử | Mở cho nghiên cứu (theo bài báo) | Mức tóm tắt |
| ViWikiFC (LREC 2026) | 20.916 claim tiếng Việt, bằng chứng Wikipedia; SUPPORTS / REFUTES / NEI | https://arxiv.org/abs/2405.07615 | Mức tóm tắt |
| ViFactCheck (AAAI 2025) | 7.232 cặp claim–bằng chứng từ báo điện tử, 12 chủ đề; Fleiss κ = 0,83 | https://ojs.aaai.org/index.php/AAAI/article/view/32008 (dữ liệu trên GitHub theo bài báo) | Mức tóm tắt |
| XNLI (cấu hình tiếng Việt) | NLI đa ngôn ngữ | Hugging Face | Chưa kiểm tra lại |

Nhãn NEI tương ứng trạng thái "bằng chứng không đủ" và cơ chế từ chối của hệ thống.

## D. OCR, layout và bảng

| Bộ dữ liệu | Nội dung | Truy cập | License |
|---|---|---|---|
| FinTabNet / FinTabNet.c | Bảng trong báo cáo thường niên S&P 500: hơn 70K trang, hơn 110K bảng. Bản gốc bị lẫn tập val/test, nên dùng bản đã sửa FinTabNet.c | https://huggingface.co/datasets/bsmock/FinTabNet.c | CDLA-Permissive-2.0 (FinTabNet.c) |
| PubTables-1M + Table Transformer | 575K trang cho phát hiện bảng; 948K bảng cho nhận dạng cấu trúc; có pretrained weights | https://github.com/microsoft/table-transformer | License dataset chưa xác nhận |
| DocLayNet | 80.863 trang, 11 lớp layout, 6 loại tài liệu, có báo cáo tài chính | https://huggingface.co/datasets/docling-project/DocLayNet | CDLA-Permissive-1.0 (một số mirror ghi "other") |
| ViNumQA (VLSP 2025) | Hơn 4.000 bộ câu hỏi–chương trình–đáp án trên bảng và văn bản; có báo cáo tài chính doanh nghiệp Việt Nam 2020–2025 | Qua shared task VLSP | Có thể cần đăng ký |
| OCR tiếng Việt | Chưa có benchmark bảng hay tài liệu scan tiếng Việt. DataStudio (Hugging Face) có hơn 2 triệu dòng văn bản tổng hợp, mô phỏng 14 kiểu nhiễu scan | Survey: https://arxiv.org/abs/2506.05061 | — |

## Lưu ý khi dùng

1. **License NC-SA:** chỉ dùng phi thương mại; dữ liệu phái sinh (ví dụ bản dịch) phải giữ cùng license.
2. **Chất lượng nhãn:** một nghiên cứu tái lập năm 2025 báo cáo vấn đề nhãn ở nhiều bộ dữ liệu khí hậu (ClimaBench). Không coi các bộ này là gold tuyệt đối.
3. **Rò rỉ vào dữ liệu huấn luyện LLM:** benchmark công khai có thể đã nằm trong dữ liệu pretraining. Kết quả tốt trên chúng không bảo đảm kết quả tốt trên báo cáo Việt Nam.
4. **Bảng:** không huấn luyện từ đầu; dùng weights có sẵn và tự gán nhãn 50–100 trang báo cáo Việt Nam để đo lỗi.
