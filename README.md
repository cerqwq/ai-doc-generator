# 📚 AI Doc Generator

AI文档生成器，支持README、API文档、技术文档生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📝 README生成
- 📖 API文档生成
- 📊 变更日志生成
- 🤝 贡献指南生成
- 📄 许可证生成
- 🔍 文档质量分析

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_doc_generator import create_tools

tools = create_tools()

# README
readme = tools.generate_readme("MyProject", "描述", features, tech_stack)

# API文档
api_docs = tools.generate_api_docs(code, "FastAPI")

# 变更日志
changelog = tools.generate_changelog(changes, "1.0.0")

# 贡献指南
contributing = tools.generate_contribution_guide("MyProject", ["Python", "FastAPI"])

# 许可证
license = tools.generate_license("MIT")

# 文档分析
analysis = tools.analyze_documentation(docs)
```

## 📁 项目结构

```
ai-doc-generator/
├── tools.py       # 文档生成器核心
└── README.md
```

## 📄 许可证

MIT License
