import { Outlet, NavLink } from "react-router-dom";

const RootLayout = () => {
  return (
    <div className="bg-blue-400 min-h-screen p-2">
      <h2>RootLayout</h2>
      <header className="p-8 w-full">
        <nav className="flex flex-row justify-between">
          <div className="flex flex-row space-x-3">
            <NavLink to="/">Home</NavLink>
            <NavLink to="/user">Dashboard</NavLink>
            <NavLink to="/transactions">Transactions</NavLink>
            <NavLink to="/categories">Categories</NavLink>
          </div>
        </nav>
      </header>
      <main className="p-8 flex flex-col flex-1 bg-white">
        <Outlet />
      </main>
    </div>
  );
};
export default RootLayout;
