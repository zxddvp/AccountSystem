import React from 'react'
import { BrowserRouter, Routes, Route } from 'react-router-dom'
import { Layout, Menu } from 'antd'
import Handbooks from './pages/Handbooks'

const { Header, Content } = Layout

export default function App() {
  return (
    <BrowserRouter>
      <Layout style={{ minHeight: '100vh' }}>
        <Header style={{ color: '#fff' }}>智能手册管理系统</Header>
        <Content style={{ padding: 24 }}>
          <Menu mode="horizontal" items={[{ key: 'handbooks', label: '手册管理' }]} />
          <Routes>
            <Route path="/" element={<div>欢迎使用</div>} />
            <Route path="/handbooks" element={<Handbooks />} />
          </Routes>
        </Content>
      </Layout>
    </BrowserRouter>
  )
}
