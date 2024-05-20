"use client";
import React from "react";

import {
  Modal,
  ModalContent,
  ModalHeader,
  ModalBody,
  Button,
  Image,
  Divider,
} from "@nextui-org/react";

import { FormatDate } from "@/utils/FormatDate";
import { IJob } from "@/utils/DataType";

interface IOpen {
  isOpen: boolean;
  onOpenChange: (isOpen: boolean) => void;
  onOpen: () => void;
  data: IJob;
}

const JobModal = ({ isOpen, onOpenChange, data, onOpen }: IOpen) => {
  return (
    <Modal isOpen={isOpen} onOpenChange={onOpenChange} size="2xl">
      <ModalContent>
        <ModalHeader>{data.title}</ModalHeader>
        <ModalBody className="flex flex-col  gap-3">
          <div className="flex items-center justify-center">
            <Image src={data.image} width={500} alt="사진" />
          </div>
          <p>{data.content}</p>
          <Divider />
          <div className="flex justify-between items-center">
            <div className="flex flex-row gap-3">
              <p>
                <strong>작성자</strong> {data.writer}
              </p>
              <p>
                <strong>작성 날짜</strong> {FormatDate(data.date)}
              </p>
            </div>
            <Button
              color="danger"
              variant="light"
              onClick={() => onOpenChange(false)}
            >
              닫기
            </Button>
          </div>
        </ModalBody>
      </ModalContent>
    </Modal>
  );
};

export default JobModal;
