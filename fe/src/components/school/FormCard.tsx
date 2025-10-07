import { ReactNode } from 'react';

type Props = {
  children: ReactNode;
};

export default function FormCard({ children }: Props) {
  return (
    <div className="bg-white p-6 rounded-lg shadow-md max-w-md w-full">
      {children}
    </div>
  );
}