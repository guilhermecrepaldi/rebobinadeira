import React from 'react'
import { Outlet, NavLink } from 'react-router-dom'

export default function Layout() {
  return (
    <div className="min-h-screen bg-gray-50">
      <nav className="bg-white shadow-sm border-b">
        <div className="max-w-7xl mx-auto px-4 flex items-center h-16 gap-8">
          <h1 className="font-bold text-lg text-gray-800">Qualidade Têxtil</h1>
          <div className="flex gap-6">
            <NavLink to="/" end className={({isActive}) => isActive ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-800'}>
              Dashboard
            </NavLink>
            <NavLink to="/defeitos" className={({isActive}) => isActive ? 'text-blue-600 font-medium' : 'text-gray-600 hover:text-gray-800'}>
              Defeitos
            </NavLink>
          </div>
        </div>
      </nav>
      <main className="max-w-7xl mx-auto px-4 py-6">
        <Outlet />
      </main>
    </div>
  )
}
