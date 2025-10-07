import { ReactNode } from 'react';

type Props = {
  children: ReactNode;
};

export default function LoginWrapper({ children }: Props) {
  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      {children}
    </div>
  );
}