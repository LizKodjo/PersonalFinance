import {
  createBrowserRouter,
  Route,
  createRoutesFromElements,
  RouterProvider,
} from "react-router-dom";
import RootLayout from "./layouts/RootLayout";
import Transactions from "./pages/transactions";
import Transaction from "./pages/transaction";
import Categories from "./pages/categories";
import UserProfile from "./pages/user";
import NotFound from "./pages/NotFound";
import RegisterPage from "./pages/register";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<RootLayout />}>
      {/* <Route index element={<Home />} /> */}
      <Route path="transactions" element={<Transactions />} />
      <Route path="user/:id" element={<UserProfile />} />
      <Route path="transaction/:id" element={<Transaction />} />
      <Route path="categories" element={<Categories />} />
      <Route path="register" element={<RegisterPage />} />
      <Route path="*" element={<NotFound />} />
    </Route>
  )
);
export default function App() {
  return <RouterProvider router={router} />;
}
