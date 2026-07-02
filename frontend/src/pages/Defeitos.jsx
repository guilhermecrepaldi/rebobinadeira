import React, { useState, useEffect } from 'react'

export default function Defeitos() {
  const [defeitos, setDefeitos] = useState([])
  const [filtro, setFiltro] = useState({ tipo: '', status: '' })

  useEffect(() => {
    const params = new URLSearchParams()
    if (filtro.tipo) params.set('tipo', filtro.tipo)
    if (filtro.status) params.set('status', filtro.status)
    fetch(`/api/defeitos/?${params}`)
      .then(r => r.json())
      .then(setDefeitos)
  }, [filtro])

  return (
    <div className="space-y-4">
      <div className="flex gap-4">
        <select className="border rounded-lg px-3 py-2" value={filtro.tipo} onChange={e => setFiltro({...filtro, tipo: e.target.value})}>
          <option value="">Todos os tipos</option>
          <option value="falha_malha">Falha Malha</option>
          <option value="marca">Marca</option>
          <option value="vinco">Vinco</option>
          <option value="irregularidade">Irregularidade</option>
          <option value="mancha">Mancha</option>
          <option value="furo">Furo</option>
        </select>
        <select className="border rounded-lg px-3 py-2" value={filtro.status} onChange={e => setFiltro({...filtro, status: e.target.value})}>
          <option value="">Todos os status</option>
          <option value="detectado">Detectado</option>
          <option value="confirmado">Confirmado</option>
          <option value="descartado">Descartado</option>
        </select>
      </div>

      <div className="bg-white rounded-xl shadow-sm border overflow-hidden">
        <table className="w-full text-sm">
          <thead className="bg-gray-50">
            <tr>
              <th className="text-left p-3">ID</th>
              <th className="text-left p-3">Tipo</th>
              <th className="text-left p-3">Severidade</th>
              <th className="text-left p-3">Status</th>
              <th className="text-left p-3">Metragem</th>
              <th className="text-left p-3">Data</th>
            </tr>
          </thead>
          <tbody>
            {defeitos.map(d => (
              <tr key={d.id} className="border-t hover:bg-gray-50">
                <td className="p-3 font-mono">{d.id}</td>
                <td className="p-3 capitalize">{d.tipo?.replace('_', ' ')}</td>
                <td className="p-3">{d.severidade?.toFixed(2)}</td>
                <td className="p-3"><span className={`px-2 py-1 rounded-full text-xs ${statusColor(d.status)}`}>{d.status}</span></td>
                <td className="p-3">{d.metragem?.toFixed(1)}m</td>
                <td className="p-3 text-gray-500">{d.created_at?.slice(0,10)}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}

function statusColor(status) {
  const map = { detectado: 'bg-yellow-100 text-yellow-800', confirmado: 'bg-blue-100 text-blue-800', descartado: 'bg-gray-100 text-gray-800' }
  return map[status] || 'bg-gray-100'
}
