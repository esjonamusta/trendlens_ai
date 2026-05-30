"""LangChain-compatible agent wrapper.

This module provides a lightweight interface for using LangChain as the LLM
backend. If LangChain is not installed, it falls back to a dummy response mode
so the project can still run and tests can pass.
"""
from typing import Any, Dict, Optional
import logging

from .base_agent import BaseAgent

logger = logging.getLogger("trendlens.langchain_agent")

try:
    from langchain.llms import OpenAI
    from langchain.prompts import PromptTemplate
except ImportError:  # pragma: no cover
    OpenAI = None  # type: ignore
    PromptTemplate = None  # type: ignore


class LangChainAgent(BaseAgent):
    def __init__(
        self,
        name: str,
        tools: Optional[Dict[str, Any]] = None,
        prompt_template: Optional[str] = None,
        llm_api_key: Optional[str] = None,
    ):
        super().__init__(name=name, tools=tools)
        self.prompt_template = prompt_template or "{input}"
        self.llm_api_key = llm_api_key
        self.llm = self._create_llm()

    def _create_llm(self):
        if OpenAI is None:
            logger.warning("LangChain/OpenAI not installed; using dummy response mode")
            return None

        if self.llm_api_key:
            return OpenAI(temperature=0, openai_api_key=self.llm_api_key)

        logger.warning("OpenAI API key not configured; using default OpenAI client")
        return OpenAI(temperature=0)

    def format_prompt(self, input_text: str) -> str:
        if PromptTemplate is None:
            return self.prompt_template.format(input=input_text)
        prompt = PromptTemplate(input_variables=["input"], template=self.prompt_template)
        return prompt.format(input=input_text)

    def run(self, input_text: str) -> Dict[str, Any]:
        payload = {"input": input_text}
        logger.info("%s running LangChain agent with input: %s", self.name, input_text)
        if self.llm is None:
            return {
                "name": self.name,
                "output": f"[DUMMY RESPONSE] Received input: {input_text}",
                "payload": payload,
            }

        prompt = self.format_prompt(input_text)
        response = self.llm(prompt)
        return {
            "name": self.name,
            "input": input_text,
            "prompt": prompt,
            "output": response,
        }
