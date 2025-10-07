import { FC } from 'react';

interface Props {
  message: string;
}

const ErrorToast: FC<Props> = ({ message }) => (
  <div className="bg-red-100 text-red-700 rounded p-2 mt-2">
    {message}
  </div>
);

export default ErrorToast;