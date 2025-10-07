import { ChangeEvent, FC } from 'react';

interface Props {
  label: string;
  type: 'username' | 'password';
  value: string;
  onChange: (e: ChangeEvent<HTMLInputElement>) => void;
}

const InputGroup: FC<Props> = ({ label, type, value, onChange }) => (
  <div className="flex flex-col gap-1">
    <label className="text-sm font-medium text-gray-700">{label}</label>
    <input
      type={type}
      value={value}
      onChange={onChange}
      className="border rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
    />
  </div>
);

export default InputGroup;