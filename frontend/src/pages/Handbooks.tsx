import React, { useEffect, useState } from 'react'
import { Table, Button, Modal, Form, Input, message } from 'antd'
import axios from 'axios'

interface Handbook {
  id: number
  name: string
  description: string
  version: string
}

export default function Handbooks() {
  const [data, setData] = useState<Handbook[]>([])
  const [loading, setLoading] = useState(false)
  const [open, setOpen] = useState(false)
  const [form] = Form.useForm()

  const fetchData = async () => {
    setLoading(true)
    try {
      const res = await axios.get('/api/handbooks/')
      setData(res.data)
    } catch (err) {
      message.error('获取手册列表失败')
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    fetchData()
  }, [])

  const handleOk = async () => {
    try {
      const values = await form.validateFields()
      await axios.post('/api/handbooks/', values)
      message.success('创建成功')
      setOpen(false)
      form.resetFields()
      fetchData()
    } catch (err) {
      message.error('创建失败')
    }
  }

  return (
    <div>
      <Button type="primary" onClick={() => setOpen(true)} style={{ marginBottom: 16 }}>
        新建手册
      </Button>
      <Table
        rowKey="id"
        loading={loading}
        dataSource={data}
        columns={[
          { title: '名称', dataIndex: 'name' },
          { title: '描述', dataIndex: 'description' },
          { title: '版本', dataIndex: 'version' }
        ]}
      />
      <Modal open={open} title="新建手册" onOk={handleOk} onCancel={() => setOpen(false)}>
        <Form form={form} layout="vertical">
          <Form.Item name="name" label="手册名称" rules={[{ required: true }]}> 
            <Input />
          </Form.Item>
          <Form.Item name="description" label="描述">
            <Input.TextArea />
          </Form.Item>
        </Form>
      </Modal>
    </div>
  )
}
