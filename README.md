# fastapi-cookiecutter
My FastAPI Template

fastapi-cookiecutter/
├── cookiecutter.json                   # 問答參數設定（模組、說明文件開關等）
├── hooks/
│   └── pre_gen_project.py              # 使用者輸入驗證
└── {{ cookiecutter.project_slug }}/    # ⬅️ 專案根目錄，將被命名為實際專案名
    ├── .gitignore                      # 忽略 pycache、venv、env 檔等
    ├── .env.example                    # 環境變數範本，.env 檔需手動建
    ├── AGENTS.md                       # CLI AI agents 說明（空檔可留空備用）
    ├── CLAUDE.md                       # Claude CLI 用法備忘（空檔可留空）
    ├── GEMINI.md                       # Gemini CLI 用法備忘（空檔可留空）
    ├── Dockerfile                      # 基本 FastAPI 容器設定（不含開發用 volume）
    ├── docker-compose.yml              # 基底設定（port、network、共通 service 等）
    ├── docker-compose.dev.yml          # ⬅️ 開發用 override 設定（volume, hot reload）
    ├── docker-compose.prod.yml         # ⬅️ 生產用 override 設定（最佳化、關掉 debug）
    ├── Makefile                        # ⬅️ 封裝啟動指令，使用 override（dev/prod 一鍵切）
    ├── pyproject.toml                  # 使用 uv 管理依賴與打包
    ├── README.md                       # 專案說明與啟動指南
    ├── alembic.ini                     # Alembic 資料庫遷移配置
    ├── app/
    │   ├── __init__.py
    │   ├── main.py                     # FastAPI app 啟動點(首頁，回應 "Hello, World!")
    │   └── core/
    │       ├── __init__.py
    │       ├── config.py               # 組態與 .env 處理邏輯
    │       ├── database.py             # 資料庫連線（如 SQLAlchemy）
    │       └── logging.py              # 統一 logging 設定格式
    ├── migrations/                     # ⬅️ Alembic 資料庫遷移文件
    │   ├── env.py                      # Alembic 環境配置
    │   ├── script.py.mako              # 新 migration 文件模板
    │   ├── versions/                   # migration 版本文件目錄
    │   └── README.md                   # migrations 使用說明
    └── tests/
        ├── conftest.py
        └── test_app.py                 # 最小單元測試，測試首頁是否正常回應
