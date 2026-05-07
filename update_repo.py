import os
import json

PROJECT_NAME = "EduCode-Agent-Architecture"

# 新增和更新的文件内容
FILES_TO_ADD = {
    "requirements.txt": """# 核心 Agent 框架
openclaw>=0.2.1
langchain>=0.1.0

# API 调用与网络通信
openai>=1.12.0  # MiMo API 兼容 OpenAI 格式
httpx>=0.26.0
pydantic>=2.5.0

# 向量检索与 RAG (规划中)
chromadb>=0.4.22
tiktoken>=0.6.0

# 本地测试工具
pytest>=8.0.0
""",

    ".gitignore": """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
.env

# IDEs
.idea/
.vscode/
*.swp
*.swo

# 本地长文本缓存 (不提交到云端)
local_context_cache/
*.log
""",

    "config.yaml": """# EduCode Agent 全局配置

llm_router:
  # 当前状态: 本地测试 (VRAM 经常溢出，处理长上下文极慢)
  # 目标状态: 等待 MiMo Orbit 计划批复后，切换至 cloud_mimo
  current_mode: "local_mock" 
  
  local_mock:
    model: "ollama/deepseek-coder"
    context_length: 8192
    
  cloud_mimo:
    model: "MiMo-V2.5-Pro"
    api_base: "https://api.xiaomimimo.com/v1"
    api_key: "${MIMO_API_KEY}" # 从环境变量读取
    context_length: 1000000 # 极度依赖的长文本能力
""",
}

# 真实业务场景的 Mock 数据
MOCK_DATA = {
    "dataset_info": "K12 C++/Python 常见逻辑与语法错误特征库 (预研阶段提取)",
    "cases": [
        {
            "id": "cpp_001",
            "language": "C++",
            "error_type": "Array Out of Bounds / Memory Leak",
            "student_code": "int arr[5];\nfor(int i=1; i<=5; i++) {\n    arr[i] = i * 10;\n}",
            "traditional_compiler_error": "Segmentation fault (core dumped)",
            "agent_diagnosis": "数组越界。C++ 数组索引从 0 开始，长度为 5 的数组最大索引为 4。循环条件 i<=5 导致访问 arr[5]，引发内存越界。",
            "socratic_hint": "同学，请观察你的数组 `arr` 定义的长度是多少？在 C++ 中，如果我们有 5 个抽屉，第一个抽屉的编号是 1 还是 0 呢？"
        },
        {
            "id": "py_001",
            "language": "Python",
            "error_type": "Scope and Indentation / Logic Flaw",
            "student_code": "def calculate_sum(n):\n    total = 0\n    for i in range(n):\n        total += i\n        return total",
            "traditional_compiler_error": "None (Returns wrong logical result silently)",
            "agent_diagnosis": "过早返回。return 语句被错误地缩进到了 for 循环内部，导致循环只执行一次就结束了函数。",
            "socratic_hint": "代码没有报错，但是结果不对哦。请仔细看一下 `return total` 这行代码前面的空格。它现在属于 for 循环的一部分，这意味着循环转了几圈就会把结果交出来呢？"
        }
    ]
}

def update_repository():
    print("🚀 正在丰富工程化文件与业务数据...")
    
    if not os.path.exists(PROJECT_NAME):
        print(f"❌ 找不到文件夹 {PROJECT_NAME}，请确保在正确的目录下运行。")
        return

    # 写入普通文件
    for filename, content in FILES_TO_ADD.items():
        filepath = os.path.join(PROJECT_NAME, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")
        print(f"📄 已生成配置文件: {filename}")

    # 创建 data 文件夹并写入 JSON 数据
    data_dir = os.path.join(PROJECT_NAME, "data")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    json_path = os.path.join(data_dir, "mock_student_errors.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(MOCK_DATA, f, ensure_ascii=False, indent=4)
    print("📊 已生成业务场景数据: data/mock_student_errors.json")

    print("\n✅ 仓库 V2 升级完毕！你的项目现在看起来非常专业。")
    print("👉 下一步：在终端中进入项目文件夹，执行以下命令同步到 GitHub：")
    print("    git add .")
    print("    git commit -m \"build: add requirements, config, and K12 mock dataset\"")
    print("    git push")

if __name__ == "__main__":
    update_repository()
