import React, { useState, useEffect } from 'react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell, LineChart, Line } from 'recharts'

const COLORS = ['#ef4444', '#f97316', '#eab308', '#22c55e', '#3b82f6']

async function api(path) {
  const res = await fetch(`/api${path}`)
  return res.json()
}

export default function Dashboard() {
  const [data, setData] = useState(null)

  useEffect(() => {
    Promise.all([
      api('/indicadores/dashboard'),
      api('/indicadores/por-tinturaria'),
      api('/indicadores/por-tipo'),
      api('/indicadores/por-data'),
    ]).then(([dashboard, tinturaria, tipos, datas]) => setData({ dashboard, tinturaria, tipos, datas }))
  }, [])

  if (!data) return <p className="text-gray-500">Carregando...</p>

  const pieData = Object.entries(data.dashboard.por_tipo || {}).map(([name, value]) => ({ name, value }))
  const lineData = (data.datas || []).map(d => ({ ...d, data: d.data?.slice(5) }))

  return (
    <div className="space-y-6">
      {/* Cards */}
      <div className="grid grid-cols-4 gap-4">
        <Card label="Total Defeitos" value={data.dashboard.total_defeitos} />
        <Card label="Lotes" value={data.dashboard.total_lotes} />
        <Card label="Pendentes" value={data.dashboard.por_status?.detectado || 0} />
        <Card label="Confirmados" value={data.dashboard.por_status?.confirmado || 0} />
      </div>

      <div className="grid grid-cols-2 gap-6">
        {/* Defeitos por tipo */}
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <h3 className="font-medium mb-3">Defeitos por Tipo</h3>
          <ResponsiveContainer width="100%" height={250}>
            <PieChart>
              <Pie data={pieData} dataKey="value" nameKey="name" cx="50%" cy="50%" outerRadius={80} label>
                {pieData.map((_, i) => <Cell key={i} fill={COLORS[i % COLORS.length]} />)}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>

        {/* Defeitos por tinturaria */}
        <div className="bg-white p-4 rounded-xl shadow-sm border">
          <h3 className="font-medium mb-3">Defeitos por Tinturaria</h3>
          <ResponsiveContainer width="100%" height={250}>
            <BarChart data={data.tinturaria}>
              <XAxis dataKey="tinturaria" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="defeitos" fill="#3b82f6" radius={[4,4,0,0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        {/* Timeline */}
        <div className="bg-white p-4 rounded-xl shadow-sm border col-span-2">
          <h3 className="font-medium mb-3">Defeitos por Dia</h3>
          <ResponsiveContainer width="100%" height={200}>
            <LineChart data={lineData}>
              <XAxis dataKey="data" />
              <YAxis />
              <Tooltip />
              <Line type="monotone" dataKey="defeitos" stroke="#3b82f6" strokeWidth={2} dot={false} />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  )
}

function Card({ label, value }) {
  return (
    <div className="bg-white p-4 rounded-xl shadow-sm border">
      <p className="text-sm text-gray-500">{label}</p>
      <p className="text-2xl font-bold mt-1">{value}</p>
    </div>
  )
}
