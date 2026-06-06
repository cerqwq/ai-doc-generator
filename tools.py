"""
AI Doc Generator - AI文档生成器
支持README、API文档、技术文档生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIDocGeneratorTools:
    """
    AI文档生成器
    支持：README、API、技术文档
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_readme(self, project_name: str, description: str, features: List[str], tech_stack: List[str]) -> str:
        """生成README"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = "\n".join(f"- {f}" for f in features)
        tech_text = "、".join(tech_stack)

        prompt = f"""请为{project_name}生成专业的README.md：

描述：{description}
特性：
{features_text}
技术栈：{tech_text}

要求：
1. Markdown格式
2. 徽章
3. 安装、使用、特性、项目结构
4. 专业且吸引人"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_api_docs(self, code: str, framework: str) -> str:
        """生成API文档"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下{framework}代码生成API文档：

{code[:2000]}

要求：
1. 端点说明
2. 参数说明
3. 返回值说明
4. 使用示例"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=3000
        )

        return response.choices[0].message.content

    def generate_changelog(self, changes: List[Dict], version: str) -> str:
        """生成变更日志"""
        if not self.client:
            return "LLM客户端未配置"

        changes_text = json.dumps(changes, ensure_ascii=False)

        prompt = f"""请根据以下变更生成CHANGELOG：

版本：{version}
变更：{changes_text}

使用Keep a Changelog格式："""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        return response.choices[0].message.content

    def generate_contribution_guide(self, project_name: str, tech_stack: List[str]) -> str:
        """生成贡献指南"""
        if not self.client:
            return "LLM客户端未配置"

        tech_text = ", ".join(tech_stack)

        prompt = f"""请为{project_name}生成CONTRIBUTING.md：

技术栈：{tech_text}

要求：
1. 开发环境
2. 代码规范
3. 提交流程
4. 测试要求"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def generate_license(self, license_type: str = "MIT") -> str:
        """生成许可证"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成{license_type}许可证文件：

要求：
1. 标准格式
2. 当前年份
3. 占位符用户名"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        return response.choices[0].message.content

    def analyze_documentation(self, docs: str) -> Dict:
        """分析文档质量"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下文档的质量：

{docs[:2000]}

请返回JSON格式：
{{
    "score": 1-100,
    "completeness": "完整性",
    "clarity": "清晰度",
    "issues": ["问题"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}


def create_tools(**kwargs) -> AIDocGeneratorTools:
    """创建文档生成器工具"""
    return AIDocGeneratorTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Doc Generator Tools")
    print()

    # 测试
    readme = tools.generate_readme("MyProject", "一个很棒的项目", ["特性1", "特性2"], ["Python", "FastAPI"])
    print(readme[:300] + "...")
