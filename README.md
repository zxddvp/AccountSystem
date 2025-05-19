# Handbook Management System

该仓库包含前后端分离的智能手册管理系统示例。

- `frontend/` 使用 React、Ant Design、Vite 和 TypeScript 构建，开发服务器运行在 **8090** 端口。
- `backend/` 使用 Django + Django REST framework，提供基本的 API。
- `docker-compose.yml` 用于同时启动前后端两个容器。

文件上传等功能通过 [ragflow](https://github.com/infiniflow/ragflow) 完成。运行后端前需要配置以下环境变量：

```bash
export RAGFLOW_BASE_URL=http://<ragflow-host>:9380
export RAGFLOW_API_KEY=<your-key>
export RAGFLOW_DATASET_ID=<optional-dataset-id>
```

## 启动方式

```bash
docker-compose up --build
```
