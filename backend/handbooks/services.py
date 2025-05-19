"""Utilities for integrating with ragflow."""

import os
from ragflow_sdk import RAGFlow


def _get_client() -> RAGFlow:
    """Create a ragflow client from environment variables."""
    base_url = os.getenv("RAGFLOW_BASE_URL")
    api_key = os.getenv("RAGFLOW_API_KEY")
    if not base_url or not api_key:
        raise RuntimeError("RAGFLOW_BASE_URL and RAGFLOW_API_KEY must be set")
    return RAGFlow(api_key=api_key, base_url=base_url)


def upload_file_to_ragflow(document):
    """Upload the document's file to ragflow if a file is available."""
    dataset_id = os.getenv("RAGFLOW_DATASET_ID")
    client = _get_client()

    if dataset_id:
        datasets = client.list_datasets(id=dataset_id)
        dataset = datasets[0] if datasets else None
    else:
        dataset = None

    if not dataset:
        dataset = client.create_dataset(name="handbook")

    if not document.file_url:
        return

    if not os.path.exists(document.file_url):
        return

    with open(document.file_url, "rb") as f:
        dataset.upload_documents([
            {"display_name": document.name, "blob": f.read()}
        ])
